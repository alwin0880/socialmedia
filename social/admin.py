from django.contrib import admin

# Register your models here.
from social.models import MyUser

admin.site.register(MyUser)