from django.contrib import admin
from .models import Car_application
from .models import Address
from .models import Car_brand
from .models import Car_const
from .models import Car_model
from .models import Car_var
from .models import Company
from .models import Office
from .models import Person
from .models import Type_of_car 

admin.site.register(Car_application)
admin.site.register(Address)
admin.site.register(Car_brand)
admin.site.register(Car_const)
admin.site.register(Car_model)
admin.site.register(Car_var)
admin.site.register(Company)
admin.site.register(Office)
admin.site.register(Person)
admin.site.register(Type_of_car)
# Register your models here.
