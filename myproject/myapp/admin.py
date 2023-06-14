from django.contrib import admin
from .models import Point


class AdminPoint(admin.ModelAdmin):
    '''
    list_filter = ('category',)
    list_display = ['name','article', 'category']
    search_fields = ['article']
    readonly_fields = ('thumbnail_preview',)
'''
    save_as = True

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True



# Register your models here.
admin.site.register(Point,AdminPoint)



# username = Tanushree, email = tanushree7252@gmail.com, password = 1234