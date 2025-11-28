from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password

from ...serializers.users import UsersSerializer
from ...data_access.users import UsersAccessor
from ...data_access.user_roles import UserRolesAccessor
from ...data_access.user_status import UserStatusAccessor
from ...data_access.user_plans import UserPlansAccessor
from ...data_access.plans import PlansAccessor


class RegisterView(APIView):
    accessor = UsersAccessor()
    role_accessor = UserRolesAccessor()
    status_accessor = UserStatusAccessor()
    user_plan_accessor = UserPlansAccessor()
    plan_accessor = PlansAccessor()

    def post(self, request):
        serializer = UsersSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data

            data["password"] = make_password(data["password"])

            role_obj = next(
                (
                    r
                    for r in self.role_accessor.get_all()
                    if r.name.lower() == "utilizator"
                ),
                None,
            )
            if not role_obj:
                return Response(
                    {"error": "User role not found"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            data["role"] = role_obj

            status_obj = next(
                (
                    s
                    for s in self.status_accessor.get_all()
                    if s.name.lower() == "activ"
                ),
                None,
            )
            if not status_obj:
                return Response(
                    {"error": "User status not found"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            data["status"] = status_obj

            user = self.accessor.add(**data)

            free_plan = next(
                (p for p in self.plan_accessor.get_all() if p.name.lower() == "buddy"),
                None,
            )
            if free_plan:
                self.user_plan_accessor.add(user=user, plan=free_plan)

            return Response(
                {
                    "message": "User created successfully",
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                        "role": role_obj.name,
                        "status": status_obj.name,
                        "created_at": user.created_at,
                        "updated_at": user.updated_at,
                        "last_login": user.last_login,
                    },
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
