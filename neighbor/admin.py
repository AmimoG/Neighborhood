from django.contrib import admin
from .models import *
from django_cascading_dropdown_widget.widgets import DjangoCascadingDropdownWidget
from django_cascading_dropdown_widget.widgets import CascadingModelchoices
from django import forms

# Register your models here.


admin.site.register(Neighborhood)
admin.site.register(Profile)
admin.site.register(Post)