
from rest_framework.viewsets import ModelViewSet

from blog1.models import Publisher
from blog1.serializer import BooksSerializer


# Create your views here.


class BooksViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = BooksSerializer
