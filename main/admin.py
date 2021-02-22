from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Course)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Register)

@admin.register(Categories)
class CatAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
	list_display_links = ['name',]

	prepopulated_fields = {'slug':('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
	list_display_links = ['name',]

	prepopulated_fields = {'slug':('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'author', 'category']
	list_display_links = ['title',]

	prepopulated_fields = {'slug':('title',)}