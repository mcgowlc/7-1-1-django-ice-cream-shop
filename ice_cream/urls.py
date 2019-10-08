from django.urls import path
from . import views

urlpatterns = [
    path('ice_cream/<int:pk>/edit/', FlavorEditView.as_view(), name='edit'),
    path('ice_cream/<int:pk>/delete/', FlavorDeleteView.as_view(), name='delete'),
    path('flavor/new/', FlavorCreateView.as_view(), name='create'),
    path('ice_cream/daily_flavors/', DailyFlavorView.as_view(), name="daily_flavors"),
    path('ice_cream/seasonal_flavors/', SeasonalFlavorView.as_view(), name="seasonal_flavors"),
    path('ice_cream/weekly_flavors/', WeeklyFlavorView.as_view(), name="weekly_flavors"),
    path('ice_cream/details/<int:pk>/', DetailsFlavorView.as_view(), name="detail"),
    path('', HomePageView.as_view(), name='home'),
]
