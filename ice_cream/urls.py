from django.urls import path
from . import views
from .views import DailyFlavorView, SeasonalFlavorView, WeeklyFlavorView, DetailsFlavorView, HomePageView

urlpatterns = [
    path('ice_cream/daily_flavors/', DailyFlavorView.as_view(), name="daily_flavors"),
    path('ice_cream/seasonal_flavors/', SeasonalFlavorView.as_view(), name="seasonal_flavors"),
    path('ice_cream/weekly_flavors/', WeeklyFlavorView.as_view(), name="weekly_flavors"),
    path('ice_cream/details/<int:pk>/', DetailsFlavorView.as_view(), name="detail"),
    path('ice_cream/featured_flavors/', HomePageView.as_view(), name="featured_flavors"),
]
