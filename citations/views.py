from django.shortcuts import render
from .models import Citation
from .serializers import CitationSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

# from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# @csrf_exempt
class CitationList(generics.ListAPIView):
    queryset = Citation.objects.all()
    serializer_class = CitationSerializer

# @csrf_exempt
class CitationDetail(generics.RetrieveAPIView):
    queryset = Citation.objects.all()
    serializer_class = CitationSerializer
    lookup_field = 'pk'

# @csrf_exempt
class CitationCreate(generics.CreateAPIView):

    def post(self, request, format=None):
        citation = CitationSerializer(data=request.data)
        if citation.is_valid():
            citation.save()
            return Response(citation.data, status=status.HTTP_201_CREATED)
        return Response(citation.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
class CitationDelete(generics.DestroyAPIView):
    queryset = Citation.objects.all()
    serializer_class = CitationSerializer
    lookup_field = 'pk'

# @csrf_exempt
class CitationUpdate(generics.UpdateAPIView):
    queryset = Citation.objects.all()
    serializer_class = CitationSerializer
    lookup_field = 'pk'

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)