from django.contrib import admin
from rango.models import Category, Page, PageAdmin, UserProfile

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

# Register your models here.
admin.site.register(Category,CategoryAdmin)
#admin.site.register(Page)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)
