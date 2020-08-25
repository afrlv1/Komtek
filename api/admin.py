from django.contrib import admin
from .models import Guide, GuideElement


class GuideAdmin(admin.ModelAdmin):
	list_display = ('name', 'title', 'version', 'date')


class GuideElementAdmin(admin.ModelAdmin):
	list_display = ('Guide', 'code', 'value')


admin.site.register(Guide, GuideAdmin)
admin.site.register(Element, GuideElementAdmin)

