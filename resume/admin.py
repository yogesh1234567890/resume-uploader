from django.contrib import admin
from .models import Resume
# Register your models here.
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    def resume(obj):
        return obj
    list_display=['resume']
    

