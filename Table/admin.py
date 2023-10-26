from django.contrib import admin
from .models import TableColumn, TableData, File
from django import forms

admin.site.register(TableData)
admin.site.register(TableColumn)
admin.site.register(File)