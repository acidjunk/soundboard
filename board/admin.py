from django.contrib import admin
from .models import SoundBoard, Sound

class SoundBoardAdmin(admin.ModelAdmin):
    """
    Class to manage SoundBoards
    """
    list_display = ('name', 'description', 'created_on', 'created_by', 'modified_on', 'modified_by')
    search_fields = ['name', 'description', 'created_by']
    list_filter = ['name', 'created_by']

class SoundAdmin(admin.ModelAdmin):
    """
    Class to manage SoundBoards
    """
    list_display = ('name', 'file', 'created_on', 'created_by', 'modified_on', 'modified_by')
    search_fields = ['name' 'created_by']
    list_filter = ['name', 'created_by']

admin.site.register(SoundBoard, SoundBoardAdmin)
admin.site.register(Sound, SoundAdmin)