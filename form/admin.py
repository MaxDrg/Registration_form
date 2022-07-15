from django.contrib import admin
from django import forms
from .models import ConfsepContent, Content

class PersonAdminForm(forms.ModelForm):
    class Meta:
        model = ConfsepContent
        fields = "__all__"

    def clean_title(self):
        data = self.cleaned_data["title"]

        return 'tester'


@admin.register(ConfsepContent)
class BookInstanceAdmin(admin.ModelAdmin):
    form = PersonAdminForm
    

admin.site.register(Content)