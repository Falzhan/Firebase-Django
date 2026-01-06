from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def format_price(value):
    """Format price as PHP with commas"""
    if value is None:
        return "N/A"
    return f"₱{value:,.2f}"

@register.filter
def get_grade_color(grade):
    """Get CSS color class for grade badges"""
    grade_colors = {
        'S': 'text-green-800 bg-green-100',
        'A': 'text-blue-800 bg-blue-100',
        'B': 'text-yellow-800 bg-yellow-100',
        'C': 'text-orange-800 bg-orange-100',
        'D': 'text-red-800 bg-red-100',
        'F': 'text-gray-800 bg-gray-100',
    }
    return grade_colors.get(grade, 'text-gray-800 bg-gray-100')

@register.filter
def get_category_icon(category):
    """Get icon class for category"""
    icon_map = {
        'AUDIO': 'fas fa-headphones',
        'PERIPHERAL': 'fas fa-mouse',
        'LAPTOP': 'fas fa-laptop',
        'MOBILE': 'fas fa-mobile-alt',
        'GADGET': 'fas fa-cogs',
    }
    return icon_map.get(category, 'fas fa-question')

@register.filter
def get_grade_badge(grade):
    """Generate HTML for grade badge"""
    colors = get_grade_color(grade)
    return mark_safe(f'<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium {colors}">{grade}</span>')

@register.filter
def format_spec_value(value):
    """Format spec values for display"""
    if value is None or value == '':
        return 'N/A'
    if isinstance(value, (int, float)):
        return f"{value}"
    return str(value)

@register.simple_tag
def wishlist_icon(is_wishlist):
    """Generate wishlist icon"""
    if is_wishlist:
        return mark_safe('<i class="fas fa-heart text-red-500"></i>')
    else:
        return mark_safe('<i class="fas fa-heart text-gray-400"></i>')

@register.filter
def price_range(price):
    """Get price range category"""
    if price is None:
        return "Unknown"
    if price < 100:
        return "Budget"
    elif price < 500:
        return "Mid-range"
    elif price < 1000:
        return "Premium"
    else:
        return "High-end"

@register.filter
def format_timestamp(timestamp):
    """Format timestamp for display"""
    if timestamp:
        return timestamp.strftime('%b %d, %Y')
    return "Unknown"

@register.filter
def spec_diff_class(value1, value2):
    """Get CSS class for spec comparison"""
    if value1 == value2 and value1 != 'N/A':
        return 'text-green-600'
    elif value1 == 'N/A' or value2 == 'N/A':
        return 'text-gray-500'
    else:
        return 'text-blue-600'