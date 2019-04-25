from django.urls import path
from .views import *

urlpatterns = [
    path('', home_render),
    path('about_us', about_us_render),
    path('riddles', riddles_render),
    path('sketches', sketches_render),
    path('join', join_render)
]
