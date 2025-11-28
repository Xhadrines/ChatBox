from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password


class GenericCRUDView(View):
    model_name = None
    accessor_class = None
    fk_fields = {}
    auto_fields = []
    password_field = None

    templates = {
        "list": "CRUD/list.html",
        "detail": "CRUD/detail.html",
        "form": "CRUD/form.html",
        "delete": "CRUD/delete.html",
    }

    list_url = ""
    detail_url_prefix = ""
    edit_url_prefix = ""
    delete_url_prefix = ""
    create_url = ""

    def get_accessor(self):
        return self.accessor_class()

    def get_columns(self):
        item = self.get_accessor().get_all().first()
        if not item:
            return []

        columns = []
        for field, value in item.__dict__.items():
            if field.startswith("_"):
                continue
            if field in self.fk_fields:
                continue
            if field in getattr(self, "auto_fields", []):
                continue
            if type(value).__name__ in (
                "int",
                "str",
                "float",
                "bool",
                "NoneType",
                "Decimal",
            ):
                columns.append(field)
        return columns

    def get_dropdowns(self):

        dropdowns = {}
        for field_name, accessor_class in self.fk_fields.items():
            accessor = accessor_class()
            dropdowns[field_name] = [
                {"id": obj.id, "display": str(obj)} for obj in accessor.get_all()
            ]
        return dropdowns

    def list(self, request):
        items = self.get_accessor().get_all()
        columns = self.get_columns()
        return render(
            request,
            self.templates["list"],
            {
                "model_name": self.model_name,
                "items": items,
                "columns": columns,
                "create_url": self.create_url,
                "detail_url_prefix": self.detail_url_prefix,
                "edit_url_prefix": self.edit_url_prefix,
                "delete_url_prefix": self.delete_url_prefix,
                "home_url": "/api-mvc/",
            },
        )

    def detail(self, request, pk):
        item = self.get_accessor().get_by_id(pk)
        fields = {
            k: (str(v) if not hasattr(v, "__dict__") else str(v))
            for k, v in item.__dict__.items()
            if not k.startswith("_")
        }
        return render(
            request,
            self.templates["detail"],
            {
                "model_name": self.model_name,
                "fields": fields,
                "list_url": self.list_url,
            },
        )

    def create(self, request):
        accessor = self.get_accessor()
        dropdowns = self.get_dropdowns()

        if request.method == "POST":
            data = request.POST.dict()

            for field, accessor_class in self.fk_fields.items():
                if field in data and data[field]:
                    fk_accessor = accessor_class()
                    data[field] = fk_accessor.get_by_id(int(data[field]))

            if self.password_field and self.password_field in data:
                data[self.password_field] = make_password(data[self.password_field])

            for key, value in list(data.items()):
                if value == "":
                    data[key] = None

            for field in self.auto_fields:
                data.pop(field, None)

            columns = self.get_columns()
            filtered_data = {
                k: v for k, v in data.items() if k in columns or k in self.fk_fields
            }

            accessor.add(**filtered_data)
            return redirect(self.list_url)

        fields = {}
        for field in self.get_columns():
            if field in self.auto_fields:
                continue
            if field in self.fk_fields:
                continue
            if field.endswith("_id"):
                continue
            if field == "id":
                continue
            fields[field] = ""

        selected_fk = {field: "" for field in self.fk_fields}

        return render(
            request,
            self.templates["form"],
            {
                "model_name": self.model_name,
                "action": "Create",
                "fields": fields,
                "dropdowns": dropdowns,
                "selected_fk": selected_fk,
                "list_url": self.list_url,
            },
        )

    def edit(self, request, pk):
        accessor = self.get_accessor()
        item = accessor.get_by_id(pk)
        dropdowns = self.get_dropdowns()

        if request.method == "POST":
            data = request.POST.dict()

            for field, accessor_class in self.fk_fields.items():
                if field in data and data[field]:
                    fk_accessor = accessor_class()
                    data[field] = fk_accessor.get_by_id(int(data[field]))

            if self.password_field and self.password_field in data:
                data[self.password_field] = make_password(data[self.password_field])

            for key, value in list(data.items()):
                if value == "":
                    data[key] = None
                if value == "None":
                    data[key] = None

            for field in self.auto_fields:
                if field in data:
                    data.pop(field)

            accessor.update(pk, **data)
            return redirect(self.list_url)

        fields = {}
        for field, value in item.__dict__.items():

            if field.startswith("_"):
                continue
            if field in self.auto_fields:
                continue
            if field in self.fk_fields:
                continue
            if field.endswith("_id"):
                continue
            if field == "id":
                continue

            if type(value).__name__ in ("int", "str", "float", "bool", "NoneType"):
                fields[field] = value

        selected_fk = {}
        for field in self.fk_fields:
            fk_obj = getattr(item, field, None)
            selected_fk[field] = fk_obj.id if fk_obj else ""

        return render(
            request,
            self.templates["form"],
            {
                "model_name": self.model_name,
                "action": "Edit",
                "fields": fields,
                "dropdowns": dropdowns,
                "selected_fk": selected_fk,
                "list_url": self.list_url,
            },
        )

    def delete(self, request, pk):
        accessor = self.get_accessor()
        item = accessor.get_by_id(pk)
        fields = {field: getattr(item, field) for field in self.get_columns()}

        if request.method == "POST":
            accessor.delete(pk)
            return redirect(self.list_url)

        return render(
            request,
            self.templates["delete"],
            {
                "model_name": self.model_name,
                "fields": fields,
                "list_url": self.list_url,
            },
        )
