from django.contrib import admin
from django import forms
from .models import ConfsepContent, Content

class PersonAdminForm(forms.ModelForm):
    class Meta:
        model = ConfsepContent
        fields = "__all__"

    def clean_checked_out_time(self):
        if self.cleaned_data["title"] == "":
            return '0000-00-00 00:00:00'
        return '0000-00-00 00:00:00'

    def clean_publish_down(self):
        if self.cleaned_data["title"] == "":
            return '0000-00-00 00:00:00'
        return '0000-00-00 00:00:00'


@admin.register(ConfsepContent)
class BookInstanceAdmin(admin.ModelAdmin):
    form = PersonAdminForm
    

admin.site.register(Content)