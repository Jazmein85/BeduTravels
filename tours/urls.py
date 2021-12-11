
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework import routers
from graphene_django.views import GraphQLView
from .esquema import schema


router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'zonas',views.ZonaViewSet)
router.register(r'tour',views.TourViewSet)

urlpatterns = [
    # Rutas para la url /api/
    path("api/", include(router.urls)),
    #Rutas para la autenticación url /api/auth/
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),

    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema)),


    path('',views.index, name="index"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/login/"), name="logout"),
]
#curl -d '{"name": "Donald", "last_name": "Mac Pato", "email":"donald@pato.org", "birthday":"2000-01-01", "gender": "H"}' -H 'Content-Type: application/json' http://localhost:8000/api/users/
#curl -X DELETE http://localhost:8000/api/users/1/
#curl -X GET http://localhost:8000/api/users/
