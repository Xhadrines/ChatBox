from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from django.utils import timezone

from ...data_access.users import UsersAccessor
from ...data_access.user_token import UserTokenAccessor
from ...data_access.user_plans import UserPlansAccessor
from ...data_access.user_status import UserStatusAccessor

from ...serializers.users import UsersSerializer


class LoginView(APIView):
    accessor = UsersAccessor()
    token_accessor = UserTokenAccessor()
    user_plans_accessor = UserPlansAccessor()
    user_status_accessor = UserStatusAccessor()

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"error": "Email and password required"}, status=400)

        user = self.accessor.get_by_email(email)
        if not user or not check_password(password, user.password):
            return Response({"error": "Invalid credentials"}, status=401)

        status = self.user_status_accessor.get_by_id(user.status_id)
        if status and status.name.lower() == "sters":
            return Response({"error": "This account has been deleted"}, status=403)

        user.last_login = timezone.now()
        user.save()

        self.user_plans_accessor.expire_plans()

        token_obj = self.token_accessor.create_or_get(user)
        serializer = UsersSerializer(user)

        return Response(
            {
                "message": "Login successful",
                "user": serializer.data,
                "token": token_obj.key,
            },
            status=200,
        )
