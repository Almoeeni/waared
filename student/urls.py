from django.urls import path,include
from . import views 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('student',views.StudentViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('age/<int:age>',views.students_under_age),
    path('email/', views.EmailView.as_view()),
]