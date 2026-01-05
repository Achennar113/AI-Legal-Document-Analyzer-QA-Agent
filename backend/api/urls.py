from django.urls import path
from .views import ingest_document, ask_question

urlpatterns = [
    path("ingest/", ingest_document),
    path("ask/", ask_question),
]
