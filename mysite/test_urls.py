#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Setup Django
django.setup()

# Now test URL resolution
from django.urls import reverse, NoReverseMatch

try:
    # Test the URL resolution
    url = reverse('poorguy:add_review')
    print(f"URL for 'poorguy:add_review': {url}")
except NoReverseMatch as e:
    print(f"Error resolving URL 'poorguy:add_review': {e}")

try:
    # Test other URLs to see if they work
    url = reverse('poorguy:tech_feed')
    print(f"URL for 'poorguy:tech_feed': {url}")
except NoReverseMatch as e:
    print(f"Error resolving URL 'poorguy:tech_feed': {e}")

try:
    url = reverse('poorguy:review_detail', args=[1])
    print(f"URL for 'poorguy:review_detail': {url}")
except NoReverseMatch as e:
    print(f"Error resolving URL 'poorguy:review_detail': {e}")