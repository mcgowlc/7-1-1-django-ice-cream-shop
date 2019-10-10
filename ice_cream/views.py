from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import IceCream

class DetailsFlavorView(DetailView):
   model = IceCream
   template_name = 'detail.html'


class DailyFlavorView(ListView):
   model = IceCream
   template_name = 'daily_flavors.html'
   queryset = IceCream.objects.filter(available='daily')

class WeeklyFlavorView(ListView):
   model = IceCream
   template_name = 'weekly_flavors.html'
   queryset = IceCream.objects.filter(available='weekly')


class SeasonalFlavorView(ListView):
   model = IceCream
   template_name = 'seasonal_flavors.html'
   queryset = IceCream.objects.filter(available='seasonal')

class FeaturedFlavorView(ListView):
    model = IceCream
    template_name = 'featured_flavors.html'
    queryset = IceCream.objects.filter(featured=True)

class FlavorCreateView(CreateView):
   model = IceCream
   template_name = 'create.html'
   fields = ['flavor', 'url', 'base', 'available', 'featured', 'date_churned']

class FlavorEditView(UpdateView):
    model = IceCream
    template_name = 'edit.html'
    fields = ['flavor', 'url', 'base', 'available', 'featured', 'date_churned']


class FlavorDeleteView(DeleteView):
   model = IceCream
   template_name = 'delete.html'
   success_url = reverse_lazy('home')
