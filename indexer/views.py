import django_filters
from django.conf import settings
from django.views.generic import ListView
from django_filters.views import FilterView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from indexer import models


class MyFilter(django_filters.FilterSet):

    class Meta:
        model = models.PostProdInstance
        fields = {
            'season': ['exact'],
            'region': ['exact'],
            'name': ['icontains'],
            'description': ['icontains'],
        }


class Index(FilterView):
    template_name = 'indexer/index.html'
    model = models.PostProdInstance
    filterset_class = MyFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["SITE"] = settings.SITE
        return context


class GetStatusAPIView(APIView):

    def get(self, request, pk):
        obj = models.PostProdInstance.objects.get(pk=pk)
        return Response(obj.is_alive, status=status.HTTP_200_OK)
