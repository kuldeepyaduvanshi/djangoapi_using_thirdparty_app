from django.contrib import admin
from api.models import Employee

# Register your models here.

@admin.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ["id","name","role","address","salary"]