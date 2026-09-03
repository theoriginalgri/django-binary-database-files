from django.urls import path

from binary_database_files import views

urlpatterns = [
    path("files/<path:name>", views.serve_mixed, name="database_file"),
]
