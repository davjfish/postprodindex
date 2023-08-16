from django.views.generic import ListView

from indexer import models


# Create your views here.

class Index(ListView):
    template_name = 'indexer/index.html'
    model = models.PostProdInstance
