from django.urls import include, path

from homeschool.core import views

app_name = "core"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("app/", views.AppView.as_view(), name="app"),
    path(
        "weekly/<int:year>/<int:month>/<int:day>/",
        views.AppView.as_view(),
        name="weekly",
    ),
    path("daily/", views.DailyView.as_view(), name="daily"),
    path(
        "daily/<int:year>/<int:month>/<int:day>/",
        views.DailyView.as_view(),
        name="daily_for_date",
    ),
    path("start/", include("homeschool.core.start_urls")),
]
