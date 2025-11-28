from django.utils import timezone
from datetime import date


def default_user_roles():
    return [
        {
            "name": "Administrator",
            "description": "Accesul e nelimitat.",
            "created_at": timezone.now(),
            "updated_at": timezone.now(),
        },
        {
            "name": "Utilizator",
            "description": "Accesul e limitat.",
            "created_at": timezone.now(),
            "updated_at": timezone.now(),
        },
    ]


def default_user_status():
    return [
        {
            "name": "Activ",
            "description": "Utilizatorul se poate conecta.",
            "created_at": timezone.now(),
            "updated_at": timezone.now(),
        },
        {
            "name": "Inactiv",
            "description": "Utilizatorul nu se poate conecta.",
            "created_at": timezone.now(),
            "updated_at": timezone.now(),
        },
        {
            "name": "Sters",
            "description": "Utilizatorul este sters logic",
            "created_at": timezone.now(),
            "updated_at": timezone.now(),
        },
    ]


def default_users():
    return [
        {
            "username": "admin",
            "email": "admin@example.com",
            "password": "Admin123",
            "role": "Administrator",
            "status": "Activ",
            "last_login": None,
            "created_at": timezone.now(),
            "updated_at": timezone.now(),
        },
        {
            "username": "user",
            "email": "user@example.com",
            "password": "User123",
            "role": "Utilizator",
            "status": "Activ",
            "last_login": None,
            "created_at": timezone.now(),
            "updated_at": timezone.now(),
        },
    ]


def default_plan_types():
    return [
        {
            "name": "Plan",
            "description": "Plata se face o singura data.",
            "created_at": timezone.now(),
            "updated_at": timezone.now(),
        },
        {
            "name": "Abonament",
            "description": "Plata se face la un anumit numar de zile.",
            "created_at": timezone.now(),
            "updated_at": timezone.now(),
        },
    ]


def default_plans():
    return [
        {
            "name": "Buddy",
            "price": "0.00",
            "type": "Plan",
            "duration_days": None,
            "name_llm_prm": "gpt-oss",
            "daily_prm_msg": 1,
            "name_llm_std": "llama3.2",
            "daily_std_msg": None,
            "daily_file_limit": 0,
            "created_at": timezone.now(),
            "updated_at": timezone.now(),
        },
        {
            "name": "Hero",
            "price": "100.00",
            "type": "Plan",
            "duration_days": None,
            "name_llm_prm": "gpt-oss",
            "daily_prm_msg": 25,
            "name_llm_std": "llama3.2",
            "daily_std_msg": None,
            "daily_file_limit": 15,
            "created_at": timezone.now(),
            "updated_at": timezone.now(),
        },
        {
            "name": "Legend",
            "price": "500.00",
            "type": "Plan",
            "duration_days": None,
            "name_llm_prm": "gpt-oss",
            "daily_prm_msg": None,
            "name_llm_std": "llama3.2",
            "daily_std_msg": None,
            "daily_file_limit": None,
            "created_at": timezone.now(),
            "updated_at": timezone.now(),
        },
        {
            "name": "Spark",
            "price": "10.00",
            "type": "Abonament",
            "duration_days": 30,
            "name_llm_prm": "gpt-oss",
            "daily_prm_msg": 5,
            "name_llm_std": "llama3.2",
            "daily_std_msg": None,
            "daily_file_limit": 1,
            "created_at": timezone.now(),
            "updated_at": timezone.now(),
        },
        {
            "name": "Turbo",
            "price": "25.00",
            "type": "Abonament",
            "duration_days": 30,
            "name_llm_prm": "gpt-oss",
            "daily_prm_msg": 10,
            "name_llm_std": "llama3.2",
            "daily_std_msg": None,
            "daily_file_limit": 5,
            "created_at": timezone.now(),
            "updated_at": timezone.now(),
        },
        {
            "name": "Ultra",
            "price": "50.00",
            "type": "Abonament",
            "duration_days": 30,
            "name_llm_prm": "gpt-oss",
            "daily_prm_msg": 15,
            "name_llm_std": "llama3.2",
            "daily_std_msg": None,
            "daily_file_limit": 10,
            "created_at": timezone.now(),
            "updated_at": timezone.now(),
        },
    ]


def default_user_plans():
    return [
        {
            "user": "admin",
            "plan": "Buddy",
            "start_date": timezone.now(),
            "end_date": None,
        },
        {
            "user": "user",
            "plan": "Legend",
            "start_date": timezone.now(),
            "end_date": None,
        },
    ]


def default_files():
    return [
        {
            "user": "user",
            "file_name": "example.txt",
            "file_path": "/files/example.txt",
            "uploaded_at": timezone.now(),
        }
    ]


def default_messages():
    return [
        {
            "user": "user",
            "user_msg": "Salut!",
            "llm_resp": "Salut!",
            "llm_used": "gpt-oss",
            "uploaded_at": timezone.now(),
        }
    ]


def default_user_usage():
    return [
        {
            "user": "user",
            "date": date.today(),
            "messages_sent": 1,
            "files_uploaded": 1,
        }
    ]
