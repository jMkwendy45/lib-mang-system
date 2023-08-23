from django.urls import path, include
from rest_framework_nested import routers

import playground
from books import views

# router = SimpleRouter()
# router.register('books', views.BookViewSet)
# router.register('authors', views.AuthorViewSet)
# router.register('reviews',views.ReviewViewSet)
# urlpatterns = [
#     path('', include(router.urls)),
#     path('', include(router.urls)),
#     path('',include(router.urls))
# ]

router = routers.DefaultRouter()
router.register('books', views.BookViewSet)
router.register('review', views.ReviewViewSet, basename='reviews')
router.register('authors', views.AuthorViewSet)

books_router = routers.NestedDefaultRouter(router, 'books', lookup='book')
books_router.register('reviews', views.ReviewViewSet, basename='book-reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('bookinstance/', views.BookInstanceViewSet.as_view())

]

# path('books/', views.BookList.as_view()),
#  # path('books/<int:pk>/', views.BookDetail.as_view()),
# path('authors/', views.AuthorDetail.as_view()),
# path('authors/<int:pk>/', views.AuthorList.as_view(), name="author-detail"),
# path('review/', views.ReviewDetail.as_view()),
# path('review/<int:pk>/', views.ReviewList.as_view(), name="review-detail"
