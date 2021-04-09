from django.urls import path 
from rest_framework_simplejwt.views import ( 
        TokenObtainPairView, 
        TokenRefreshView, 
    ) 
from django.urls import include, path  
from rest_framework.authtoken import views  
from rest_framework.routers import DefaultRouter  
from api.views import NewsList
  
 
router = DefaultRouter()  

router.register( 
    'news', NewsList, basename ='news_list' 
    ) 

  
urlpatterns = [ 
        path( 
            'v1/auth/',  
            TokenObtainPairView.as_view(),  
            name='token_obtain_pair' 
        ), 
        path( 
            'v1/auth/refresh/',  
            TokenRefreshView.as_view(),  
            name='token_refresh' 
        ),  
        path('v1/', include(router.urls)),    
    ] 
    