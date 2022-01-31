from django.contrib import admin
from .models import Employers, Post, Status, Insurance
# Register your models here.

admin.site.register(Employers)
admin.site.register(Post)
admin.site.register(Status)
admin.site.register(Insurance)