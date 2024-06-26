from django.urls import include, path
from .views import *

urlpatterns = [
    path("", CitationList.as_view(), name='get_citations' ),
    path("<int:pk>", CitationDetail.as_view(), name='get_citation' ),
    path("create", CitationCreate.as_view(), name='create_citation'),
    path('edit/<int:pk>/', CitationUpdate.as_view(), name='citation_update'),
    path('delete/<int:pk>/', CitationDelete.as_view(), name='citation_delete'),
]