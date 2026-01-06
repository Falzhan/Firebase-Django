from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    # Basic Information
    title = models.CharField(max_length=200, help_text="Product name or review title")
    
    # The "Poor Guy" Filter
    price_php = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text="Price in USD",
        validators=[MinValueValidator(0)]
    )
    
    # Grading System
    GRADE_CHOICES = [
        ('S', 'S-Tier'),
        ('A', 'A-Tier'), 
        ('B', 'B-Tier'),
        ('C', 'C-Tier'),
        ('D', 'D-Tier'),
        ('F', 'F-Tier'),
    ]
    grade = models.CharField(
        max_length=1, 
        choices=GRADE_CHOICES,
        default='B',
        help_text="Overall rating of the product"
    )
    
    # The Tech Logic
    CATEGORY_CHOICES = [
        ('AUDIO', 'Audio'),
        ('PERIPHERAL', 'Peripheral'),
        ('LAPTOP', 'Laptop'),
        ('MOBILE', 'Mobile'),
        ('GADGET', 'Gadget'),
    ]
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='AUDIO',
        help_text="Type of tech product"
    )
    
    # Detailed Specifications (JSON Field)
    specs = models.JSONField(
        default=dict,
        help_text='Product specifications as JSON. Example: {"impedance": "32", "driver": "50mm"}'
    )
    
    # Media
    cover_image = models.ImageField(
        upload_to='poorguy/covers/',
        blank=True,
        null=True,
        help_text="Product cover image"
    )
    
    # Content
    verdict = models.TextField(
        help_text="The TL;DR summary - what you should know"
    )
    content = models.TextField(
        help_text="Full review body with detailed analysis"
    )
    
    # Features
    is_wishlist = models.BooleanField(
        default=False,
        help_text="Is this item on your wishlist?"
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Tech Review'
        verbose_name_plural = 'Tech Reviews'
    
    def __str__(self):
        return f"{self.title} ({self.get_grade_display()})"
    
    def get_price_display(self):
        """Format price with $ symbol"""
        return f"${self.price_php:,.2f}"
    
    def get_spec_keys(self):
        """Get sorted list of spec keys"""
        return sorted(self.specs.keys()) if self.specs else []
    
    def get_spec_value(self, key):
        """Get spec value by key"""
        return self.specs.get(key, 'N/A')