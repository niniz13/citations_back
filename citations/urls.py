from django.urls import include, path
from .views import *

urlpatterns = [
    path("", CitationList.as_view(), name='get_citations' ),
    path("create", CitationCreate.as_view(), name='create_citation'),
    path('delete/<int:pk>/', CitationDelete.as_view(), name='citation_delete'),
]