from django.contrib import admin
from django.urls import path
from app import views
from rest_framework.urlpatterns import format_suffix_patterns

# viewset-------------
from django.urls.conf import include
from app.views import StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('student', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls))
]


# urlpatterns = format_suffix_patterns([
    # path('apilist/', views.api_list),
    # path('apidetail/<int:pk>', views.api_detail),

# class api_view
    # path('apilist/', views.api_list),
    # path('apidetail/<int:pk>', views.api_detail),

# class base view path
    # path('myapi/', views.BlogList.as_view()),
    # path('detail/<int:pk>/', views.ApiDetail.as_view()),

#mixinc url path
    # path('gav/', views.StudentList.as_view(), name='student-list'),
    # path('mydetail/<int:pk>/', views.StudentDetail.as_view()),

# hyperlink api path function base
    # path('', views.api_root),
    
# ])