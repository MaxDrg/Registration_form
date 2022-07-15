from django.contrib import admin
from django import forms
from .models import ConfsepContent, Content

class PersonAdminForm(forms.ModelForm):
    class Meta:
        model = ConfsepContent
        fields = "__all__"

    def clean_first_name(self):
        if self.cleaned_data["title"] == "Spike":
            raise forms.ValidationError("No Vampires")

        return self.cleaned_data["first_name"]


@admin.register(ConfsepContent)
class BookInstanceAdmin(admin.ModelAdmin):
    form = PersonAdminForm
    

admin.site.register(Content)