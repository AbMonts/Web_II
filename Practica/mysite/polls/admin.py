from django.contrib import admin
#pa que se pueda modificar
from .models import Question

admin.site.register(Question)