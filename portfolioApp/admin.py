from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Customer)
admin.site.register(Content)
admin.site.register(Photo)
admin.site.register(MakeUp)
admin.site.register(Portfolio)
admin.site.register(Payment)
admin.site.register(Card)