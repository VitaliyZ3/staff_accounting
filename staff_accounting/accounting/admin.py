from django.contrib import admin
from .models import Employer, Post, Status, Insurance
# Register your models here.

admin.site.register(Employer)
admin.site.register(Post)
admin.site.register(Status)
admin.site.register(Insurance)