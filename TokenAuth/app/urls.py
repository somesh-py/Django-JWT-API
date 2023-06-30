from django.urls import path,include
from rest_framework import routers
from .views import CarAPI
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

routers=routers.DefaultRouter()

routers.register(r'CarAPI',CarAPI,basename='CarAPI')

urlpatterns = [
    path('',include(routers.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
    path('tokenverify/',TokenVerifyView.as_view(),name='token_verify'),
]

# http POST http://127.0.0.1:8000/gettoken/ username="jwttoken" password="sanjeev123"
# curl -X POST -d "username=jwttoken&password=sanjeev123" http://127.0.0.1:8000/gettoken/
# curl \-X POST \-H "Content-Type: application/json" \-d '{"username": "somesh1", "password": "someshsharma12"}' \http://localhost:8000/api/token/
# curl \-X POST \-H "Content-Type: application/json" \-d '{"username": "somesh1", "password": "someshsharma12"}' \http://localhost:8000/api/token/
# http://localhost:8000/gettoken/