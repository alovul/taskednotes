from django.urls import path
from notes import views
from notes.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="notes/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("log/", views.log_message, name="log"),
]