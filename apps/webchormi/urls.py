from django.urls import path
from .views import chormi


urlpatterns = {
    path('', chormi, name='chormi'),
}
