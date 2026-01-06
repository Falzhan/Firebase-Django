from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'title', 
        'get_price_display', 
        'grade', 
        'category', 
        'is_wishlist',
        'created_at'
    ]
    list_filter = ['grade', 'category', 'is_wishlist', 'created_at']
    search_fields = ['title', 'verdict', 'content']
    list_editable = ['grade', 'is_wishlist']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        (None, {
            'fields': ('title', 'price_php', 'grade', 'category')
        }),
        ('Specifications', {
            'fields': ('specs',)
        }),
        ('Content', {
            'fields': ('verdict', 'content')
        }),
        ('Media & Features', {
            'fields': ('cover_image', 'is_wishlist')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    def get_price_display(self, obj):
        return obj.get_price_display()
    get_price_display.short_description = 'Price (PHP)'
    get_price_display.admin_order_field = 'price_php'