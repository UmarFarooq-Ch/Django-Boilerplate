from django.urls import path, include

urlpatterns = [
    path('users/', include('root.v1.users.urls'))
]