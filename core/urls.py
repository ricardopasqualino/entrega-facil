
from django.contrib import admin # Importa o modulo de login do Django
from django.urls import include, path # Importa as funções do path e include


from delivery.views import ( 
    Morador_novo, 
    Login_view, 
    Logout_view, 
    Password_reset, 
    Register,
)


urlpatterns = [

    # My apps
    path('',include('main.urls')),
    path('',include('delivery.urls')),
    path('',include('guests.urls')),
    path('',include('parking.urls')),
    path('',include('resident.urls')),

    # Authentication
    path('admin/', admin.site.urls, name='Admin'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', Login_view , name='Login'),
    path('logout/', Logout_view , name='Logout'),
    path('reset-senha/', Password_reset , name='Password_reset'),
    path('cadastro/', Morador_novo , name='Morador_novo'),
    path('acesso/', Register , name='Register'),

]