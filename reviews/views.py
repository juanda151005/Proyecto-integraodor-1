from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

def reviews(request):
    reviewss = Reviews.objects.all().order_by('-general_rate')
    return render(request, 'reviews.html', {'reviewss':reviewss})

@login_required
def create_review(request, city_name):
    if request.method == 'GET':
        form = ReviewForm(initial={'city': city_name})
        return render(request, 'create_review.html', {'form': form, 'city_name': city_name})
    else:
        try:
            form = ReviewForm(request.POST)
            if form.is_valid():
                new_review = form.save(commit=False)
                new_review.user = request.user  
                new_review.city = city_name  
                new_review.save()  
                return redirect('reviews')  
            else:
                return render(request, 'create_review.html', {'form': form, 'city_name': city_name, 'error': 'Datos del formulario no válidos'})
        except Exception as e:
            return render(request, 'create_review.html', {'form': form, 'city_name': city_name, 'error': f'Error al crear la reseña: {e}'})


def show_reply_reviews(request, review_id):
    reviews = get_object_or_404(Reviews, pk=review_id)
    replies=ReplyReview.objects.all().filter(review_id=review_id)
    return render(request, 'show_reply_reviews.html',{'replies':replies,'review':reviews}) 

@login_required
def create_reply_review(request, review_id):
    review = get_object_or_404(Reviews, pk=review_id) 
    if request.method == 'POST':
        form = ReplyReviewForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user 
            reply.review = review  
            reply.save() 
            return redirect('reviews') 
    else:
        form = ReplyReviewForm()

    return render(request, 'create_reply_review.html', {'form': form, 'review': review})