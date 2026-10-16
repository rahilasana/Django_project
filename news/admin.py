from django.contrib import admin

# Register your models here.

from .models import News,Product


# Register the News model in the Django Admin Panel
@admin.register(News)

# Customize how News records appear in the Admin Panel
class NewsAdmin(admin.ModelAdmin):

    # Display title and creation date as columns in the news list
    list_display = ('title', 'created_at')

    # Enable searching news by its title
    search_fields = ('title',)
    
# admin.site.register(News)

admin.site.register(Product)

