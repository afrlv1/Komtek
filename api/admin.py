from django.contrib import admin
from .models import Guide, Element


class GuideAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'version', 'date')


class ElementAdmin(admin.ModelAdmin):
    list_display = ('guide', 'code', 'value')


admin.site.register(Guide, GuideAdmin)
admin.site.register(Element, ElementAdmin)
