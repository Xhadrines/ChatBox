from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from django.contrib.auth.hashers import check_password

from common.models.users import Users


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["endpoints"] = [
            ("API ORM Schema First", "/api-orm/sf/"),
            ("API ORM Code First", "/api-orm/cf/"),
            ("API MVC", "/login/"),
            ("API", "/api/"),
        ]

        return context


class LoginView(View):
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            return render(
                request, self.template_name, {"error": "Credentiale invalide"}
            )

        if not check_password(password, user.password):
            return render(
                request, self.template_name, {"error": "Credentiale invalide"}
            )

        if user.role.name.lower() != "administrator":
            return render(
                request,
                self.template_name,
                {"error": "Nu ai drepturi de administrator"},
            )

        request.session["user_id"] = user.id
        request.session["username"] = user.username
        request.session["role"] = user.role.name

        user.last_login = timezone.now()
        user.save()

        return redirect("/api-mvc/")


from django.shortcuts import redirect


def logout_view(request):
    request.session.flush()
    return redirect("/")
