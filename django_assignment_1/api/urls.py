from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('country/',views.CountryList.as_view()),
    path('country/<int:pk>/',views.CountryDetail.as_view()),
    path('state/',views.StateList.as_view()),
    path('state/<int:pk>/',views.StateDetail.as_view()),
    path('city/',views.CityList.as_view()),
    path('city/<int:pk>/',views.CityDetail.as_view()),
    path('town/', views.TownList.as_view()),
    path('town/<int:pk>/', views.TownDetail.as_view()),
    path('person/', views.PersonList.as_view()),
    path('person/<int:pk>/', views.PersonDetail.as_view()),
    path('person/paginated/', views.PersonPagination.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)