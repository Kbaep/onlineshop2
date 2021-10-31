from django.contrib import admin
from account.models import UserProfile, TypeUserProfile

# Register your models here.

admin.site.register(TypeUserProfile)
admin.site.register(UserProfile)

