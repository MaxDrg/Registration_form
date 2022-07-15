from django.contrib import admin
from .models import ConfsepContent, Content


@admin.register(ConfsepContent)
class BookInstanceAdmin(admin.ModelAdmin):
    readonly_fields = ('title', 'images')

admin.site.register(Content)