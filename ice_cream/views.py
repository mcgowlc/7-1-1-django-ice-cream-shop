from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import IceCream


class HomePageView(ListView):
   model = IceCream
   template_name = 'home.html'


class DetailsFlavorView(DetailView):
   model = IceCream
   template_name = 'detail.html'


class DailyFlavorView(ListView):
   model = IceCream
   template_name = 'daily_flavors.html'


class WeeklyFlavorView(ListView):
   model = IceCream
   template_name = 'weekly_flavors.html'



class SeasonalFlavorView(ListView):
   model = IceCream
   template_name = 'seasonal_flavors.html'

class FeaturedFlavorView(ListView):
    model = IceCream
    template_name = 'home.html'
