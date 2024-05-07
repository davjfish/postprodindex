from django.conf import settings
from django.views.generic import ListView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from indexer import models


# Create your views here.

class Index(ListView):
    template_name = 'indexer/index.html'
    model = models.PostProdInstance
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["SITE"] = settings.SITE
        return context


class GetStatusAPIView(APIView):

    def get(self, request, pk):
        obj = models.PostProdInstance.objects.get(pk=pk)
        return Response(obj.is_alive, status=status.HTTP_200_OK)

