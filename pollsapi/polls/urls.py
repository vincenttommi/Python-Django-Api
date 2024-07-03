from django.urls import path
from .views  import polls_list,polls_detail
from . import views

urlpatterns = [
    path("polls/", polls_list, name="polls_list"),
    path("polls/<int:pk>/", polls_list, name="polls_detail")
]
