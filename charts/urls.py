from django.urls import path
from . import views


# rest_framwork imports
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('bar', views.bar_chart)

urlpatterns = [
    path('candle/', views.candle_chart),
    path('bar/', views.bar_chart),
    path('line/', views.line_chart),
    path('pie/', views.pie_chart),
]
