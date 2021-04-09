from rest_framework import permissions, generics 
from rest_framework.viewsets import ViewSetMixin 
from .serializers import NewsSerializer 
from .models import News


class NewsList(ViewSetMixin, generics.ListAPIView):  
 
    queryset = News.objects.all()  
    serializer_class = NewsSerializer  
    permission_classes = [permissions.IsAuthenticated]  
