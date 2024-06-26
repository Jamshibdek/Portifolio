
from django.urls import path
from .views import Umumiy, contact_view
urlpatterns = [
    path('', Umumiy.as_view(), name="homepage"),
    path('contact/', contact_view, name='contact'),

]
