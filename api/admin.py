from django.contrib import admin
from .models import Guide, Element


class GuideAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'version', 'date')
    search_fields = ('name', 'title')
    list_filter = ('date',)

class ElementAdmin(admin.ModelAdmin):
    list_display = ('guide', 'code', 'value')
    search_fields = ('guide', 'code')
    list_filter = ('guide',)


admin.site.register(Guide, GuideAdmin)
admin.site.register(Element, ElementAdmin)
