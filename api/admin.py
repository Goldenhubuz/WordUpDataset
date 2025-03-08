from django.contrib import admin

from .models import Word

class BaseAdmin(admin.ModelAdmin):
    list_per_page = 10

    class Meta:
        abstract = True

class WordAdmin(BaseAdmin):
    list_display = [f.name for f in Word._meta.fields]


admin.site.register(Word, WordAdmin)