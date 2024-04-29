from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact', 'operator', 'email')  # Columns to display in admin
    search_fields = ('user__username', 'contact', 'email')  # Fields for search functionality
    list_filter = ('operator',)  # Filters for admin interface

admin.site.register(Profile, ProfileAdmin)




from django.contrib import admin
from .models import Campaign, Prize, Quiz, Participation

admin.site.register(Campaign)
admin.site.register(Participation)
admin.site.register(Prize)
admin.site.register(Quiz)
