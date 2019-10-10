from django.urls import path
from . import views
from .views import DailyFlavorView, SeasonalFlavorView, WeeklyFlavorView, DetailsFlavorView, FeaturedFlavorView

app_name = "ice_cream"

urlpatterns = [
    path('daily_flavors/', DailyFlavorView.as_view(), name="daily_flavors"),
    path('seasonal_flavors/', SeasonalFlavorView.as_view(), name="seasonal_flavors"),
    path('weekly_flavors/', WeeklyFlavorView.as_view(), name="weekly_flavors"),
    path('details/<int:pk>/', DetailsFlavorView.as_view(), name="detail"),
    path('', FeaturedFlavorView.as_view(), name="featured_flavors"),
]
