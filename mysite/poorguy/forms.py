from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'title', 'price_php', 'grade', 'category', 
            'specs', 'cover_image', 'verdict', 'content', 'is_wishlist'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Enter product name or review title'
            }),
            'price_php': forms.NumberInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'step': '0.01',
                'placeholder': 'Enter price in PHP (e.g., 1299.99)'
            }),
            'grade': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
            'specs': forms.Textarea(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'rows': 4,
                'placeholder': 'Enter specifications as JSON. Example: {"impedance": "32", "driver": "50mm"}'
            }),
            'verdict': forms.Textarea(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'rows': 3,
                'placeholder': 'The TL;DR summary - what you should know'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'rows': 8,
                'placeholder': 'Full review body with detailed analysis'
            }),
            'is_wishlist': forms.CheckboxInput(attrs={
                'class': 'mr-2'
            }),
        }
        
        labels = {
            'title': 'Product Title',
            'price_php': 'Price (PHP)',
            'grade': 'Overall Grade',
            'category': 'Product Category',
            'specs': 'Specifications (JSON)',
            'cover_image': 'Cover Image',
            'verdict': 'Quick Verdict',
            'content': 'Full Review',
            'is_wishlist': 'Add to Wishlist',
        }