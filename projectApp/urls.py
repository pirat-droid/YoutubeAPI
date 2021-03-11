from django.urls import path
from .views import population_chart, home

urlpatterns = [
    # path('', line_chart, name='line_chart'),
    # path('chartJSON', line_chart_json, name='line_chart_json'),
    path('', home, name='home'),
    path('population-chart/', population_chart, name='population-chart'),
]
