from django.contrib import admin
from .models import Tweet
from django.contrib.auth.decorators import login_required

# Register your models here.
admin.site.register(Tweet)
admin.site.login = login_required(admin.site.login)
