from django.urls import path
from . import views

urlpatterns=[
    path('',views.reviews,name='reviews'),
    path('create_review/<str:city_name>/', views.create_review, name='create_review'),
    path('reviews/<int:review_id>/show_replies/', views.show_reply_reviews, name='show_reply_reviews'),
    path('reviews/<int:review_id>/reply/', views.create_reply_review, name='create_reply_review'),
]
