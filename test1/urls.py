from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from test1 import views


urlpatterns = [
    path("snippets/", views.snippet_list),
    path("snippet/<int:pk>/", views.snippet_detail)
]


urlpatterns = format_suffix_patterns(urlpatterns)