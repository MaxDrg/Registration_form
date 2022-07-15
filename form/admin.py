from django.contrib import admin
from .models import ConfsepContent, Content


@admin.register(ConfsepContent)
class BookInstanceAdmin(admin.ModelAdmin):
    readonly_fields = ('checked_out_time',)

    def my_custom_field(self, obj):
        return 'Return Anything Here'
    

admin.site.register(Content)