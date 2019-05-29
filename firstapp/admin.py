from django.contrib import admin
from firstapp.models import UserRole
# Register your models here.
admin.site.register(UserRole)
#now superuser can create,delete amd manage this table
#to create superuser python manage.py createsuperuser
#password-jindchahal@007
