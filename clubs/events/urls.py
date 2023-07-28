from events import views
from django.urls import path

urlpatterns = [
        path('', views.home, name="home"),
        path('<int:year>/<str:month>/', views.home, name='home'),
        path('events/', views.all_events, name="events-list"),
        path('add_venue/', views.add_venue, name="add-venue"),
        path('list_venue/', views.list_venue, name="list-venue"),
        path('show_venue/<venue_id>', views.show_venue, name="show-venue"),
        path('search_venue/', views.search_venue, name="search-venue"),
        path('update_venue/<venue_id>', views.update_venue, name="update-venue"),
        path('add_event/', views.add_event, name="add-event"),
        path('update_event/<event_id>', views.update_event, name="update-event")
]
