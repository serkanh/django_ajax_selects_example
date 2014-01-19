from django.contrib import admin
from links.models import Link, Tag

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    pass
class TagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Link, LinkAdmin)
admin.site.register(Tag, TagAdmin)