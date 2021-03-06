from xml.parsers.expat import model
from django.contrib import admin
from .models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Post, PostAdmin)
admin.site.register(Trip)
admin.site.register(Site)
admin.site.register(Destination)
admin.site.register(Owner)
admin.site.register(Dog)
