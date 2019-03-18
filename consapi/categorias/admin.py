from django.contrib import admin

# Register your models here.

from .models import Categorias
    
#from .models import Locales
#from .models import Canchas
#from .models import Reservas

admin.site.register(Categorias)

#admin.site.register(Locales)
#admin.site.register(Canchas)
#admin.site.register(Reservas)