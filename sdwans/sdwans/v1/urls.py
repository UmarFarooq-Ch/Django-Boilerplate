from django.urls import path, include

urlpatterns = [
    path('users/', include('sdwans.v1.users.urls'))
]