from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# namespace
app_name = 'events'

urlpatterns = [
    # Create an event
    path('create/', views.TaskCreateView.as_view(), name='event_create'),
    # Retrieve event list
    path('', views.TaskListView.as_view(), name='event_list'),
    # Retrieve single event object
    re_path(r'^(?P<pk>\d+)/$', views.TaskDetailView.as_view(), name='event_detail'),
    # Update an event
    re_path(r'^(?P<pk>\d+)/update/$', views.TaskUpdateView.as_view(), name='event_update'),
    # Delete an event
    re_path(r'^(?P<pk>\d+)/delete/$', views.TaskDeleteView.as_view(), name='event_delete')
    # Login
]

urlpatterns += staticfiles_urlpatterns()