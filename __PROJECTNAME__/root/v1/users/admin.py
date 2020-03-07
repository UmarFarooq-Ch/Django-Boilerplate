from django.contrib import admin

# Register your models here.
from root.v1.users.models import User

admin.sites.register(User)
