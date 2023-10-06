
# from django.urls import path
# from . import views

# app_name = 'Bug'

# urlpatterns = [

#     # path('', views.IndexView.as_view(), name='index'),
#     path('register/<int:pk>/', views.BugRegistrationView.as_view(), name='register_bug'),
#     path('<int:pk>/', views.BugDetailView.as_view(), name='view_bug'),
#     path('list/', views.BugListView.as_view(), name='list_bug'),
# ]

from django.urls import path
from . import views

app_name = 'Bug'

urlpatterns = [
    path("", views.index, name="index"),
    path('register/<int:pk>/', views.register_bug, name='register_bug'),
    path('<int:bug_id>/', views.view_bug, name='view_bug'),
    path('list/', views.list_bug, name='list_bug'),
]
