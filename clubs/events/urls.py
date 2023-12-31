from events import views
from django.urls import path

urlpatterns = [
        path('', views.home, name="home"),
        path('<int:year>/<str:month>/', views.home, name='home'),
        path('events/', views.all_events, name="list-event"),
        path('user_events/', views.user_events, name='user-event'),
        path('user_going_events/', views.user_going_events, name="user-going-event"),
        path('add_event/', views.add_event, name="add-event"),
        path('update_event/<event_id>', views.update_event, name="update-event"),
        path('delete_event/<event_id>', views.delete_event, name="delete-event"),
        path('search_event/', views.search_event, name="search-event"),
        path('add_venue/', views.add_venue, name="add-venue"),
        path('list_venue/', views.list_venue, name="list-venue"),
        path('show_venue/<venue_id>', views.show_venue, name="show-venue"),
        path('search_venue/', views.search_venue, name="search-venue"),
        path('update_venue/<venue_id>', views.update_venue, name="update-venue"),
        path('delete_venue/<venue_id>', views.delete_venue, name="delete-venue"),
        path('venue_text/', views.venue_text, name="venue-text"),
        path('venue_csv/', views.venue_csv, name="venue-csv"),
        path('venue_pdf/', views.venue_pdf, name="venue-pdf")
]
