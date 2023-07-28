from events import views
from django.urls import path

urlpatterns = [
        path('', views.home, name="home"),
        path('<int:year>/<str:month>/', views.home, name='home'),
        path('events/', views.all_events, name="events-list"),
        path('add_venue/', views.add_venue, name="add-venue")
]
