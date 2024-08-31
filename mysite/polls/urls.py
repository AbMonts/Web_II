from django.urls import include, path


from . import views

urlpatterns = [
    # Define tus rutas aquí
    path('', views.index, name='index'),  # Ejemplo: Ruta para la vista 'index'
    
]
