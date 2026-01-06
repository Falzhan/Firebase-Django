from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Review
from .forms import ReviewForm

def tech_feed(request):
    """
    Main tech blog feed view.
    Shows wishlist items at top (horizontal scroll)
    Shows reviewed gear below (responsive grid)
    """
    # Get sorting parameters
    wishlist_sort = request.GET.get('wishlist_sort', 'created_at')
    wishlist_order = request.GET.get('wishlist_order', 'desc')
    
    # Build wishlist queryset with sorting
    wishlist_items = Review.objects.filter(is_wishlist=True)
    
    if wishlist_sort == 'rating':
        wishlist_items = wishlist_items.order_by(f'{"-" if wishlist_order == "desc" else ""}grade', '-created_at')
    elif wishlist_sort == 'price':
        wishlist_items = wishlist_items.order_by(f'{"-" if wishlist_order == "desc" else ""}price_php', '-created_at')
    else:
        wishlist_items = wishlist_items.order_by(f'{"-" if wishlist_order == "desc" else ""}created_at')
    
    # Get reviewed items with category filtering
    category = request.GET.get('category')
    reviewed_items = Review.objects.filter(is_wishlist=False)
    
    if category:
        reviewed_items = reviewed_items.filter(category=category)
    
    reviewed_items = reviewed_items.order_by('-created_at')
    
    context = {
        'wishlist_items': wishlist_items,
        'reviewed_items': reviewed_items,
        'wishlist_sort': wishlist_sort,
        'wishlist_order': wishlist_order,
        'category': category,
    }
    
    return render(request, 'poorguy/review_grid.html', context)

def review_detail(request, review_id):
    """
    Single product review detail view
    """
    review = get_object_or_404(Review, id=review_id)
    context = {
        'review': review,
    }
    return render(request, 'poorguy/review_detail.html', context)

def compare_specs(request):
    """
    Compare specs between two products
    Takes two review IDs from GET parameters
    If only one ID is provided, show selection interface for second product
    """
    review_id1 = request.GET.get('id1')
    review_id2 = request.GET.get('id2')
    
    # Get all reviewed items for the selection dropdown
    reviewed_items = Review.objects.filter(is_wishlist=False).order_by('-created_at')
    
    if review_id1 and review_id2:
        # Both products selected, perform comparison
        try:
            review1 = Review.objects.get(id=review_id1)
            review2 = Review.objects.get(id=review_id2)
        except Review.DoesNotExist:
            return JsonResponse({'error': 'One or both reviews not found'}, status=404)
        
        # Get all unique spec keys from both reviews
        all_spec_keys = set(review1.get_spec_keys()) | set(review2.get_spec_keys())
        sorted_keys = sorted(all_spec_keys)
        
        comparison_data = []
        for key in sorted_keys:
            value1 = review1.get_spec_value(key)
            value2 = review2.get_spec_value(key)
            comparison_data.append({
                'key': key,
                'value1': value1,
                'value2': value2,
                'same': value1 == value2
            })
        
        context = {
            'review1': review1,
            'review2': review2,
            'comparison_data': comparison_data,
            'reviewed_items': reviewed_items,
        }
        
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'review1_title': review1.title,
                'review2_title': review2.title,
                'comparison_data': comparison_data,
            })
        
        return render(request, 'poorguy/compare_specs.html', context)
    
    elif review_id1:
        # Only first product selected, show selection interface
        try:
            review1 = Review.objects.get(id=review_id1)
        except Review.DoesNotExist:
            return JsonResponse({'error': 'Review not found'}, status=404)
        
        context = {
            'review1': review1,
            'reviewed_items': reviewed_items,
        }
        
        return render(request, 'poorguy/compare_specs.html', context)
    
    else:
        # No products selected, show empty interface
        context = {
            'reviewed_items': reviewed_items,
        }
        
        return render(request, 'poorguy/compare_specs.html', context)

def category_filter(request, category_slug):
    """
    Filter reviews by category
    """
    reviews = Review.objects.filter(category=category_slug, is_wishlist=False).order_by('-created_at')
    context = {
        'reviews': reviews,
        'category': category_slug,
    }
    return render(request, 'poorguy/category_filter.html', context)

def grade_filter(request, grade):
    """
    Filter reviews by grade
    """
    reviews = Review.objects.filter(grade=grade, is_wishlist=False).order_by('-created_at')
    context = {
        'reviews': reviews,
        'grade': grade,
    }
    return render(request, 'poorguy/grade_filter.html', context)

# CRUD Views
def add_review(request):
    """
    Add a new review
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review added successfully!')
            return redirect('poorguy:tech_feed')
    else:
        form = ReviewForm()
    
    context = {
        'form': form,
        'title': 'Add New Review',
        'action': 'Add',
    }
    return render(request, 'poorguy/review_form.html', context)

def edit_review(request, review_id):
    """
    Edit an existing review
    """
    review = get_object_or_404(Review, id=review_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review updated successfully!')
            return redirect('poorguy:review_detail', review_id=review.id)
    else:
        form = ReviewForm(instance=review)
    
    context = {
        'form': form,
        'title': f'Edit {review.title}',
        'action': 'Update',
        'review': review,
    }
    return render(request, 'poorguy/review_form.html', context)

def delete_review(request, review_id):
    """
    Delete a review with confirmation
    """
    review = get_object_or_404(Review, id=review_id)
    
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Review deleted successfully!')
        return redirect('poorguy:tech_feed')
    
    context = {
        'review': review,
    }
    return render(request, 'poorguy/review_confirm_delete.html', context)