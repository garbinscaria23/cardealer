from django.contrib import admin
from .models import Contact,feedback

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'car_title', 'city', 'create_date')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'car_title')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    # Your custom admin configuration for the Feedback model
    pass

# admin.site.register(Contact, ContactAdmin)
admin.site.register(feedback, FeedbackAdmin)

