from django.contrib import admin

from .models import Woodwork, Like, Order, Rating, WoodworkImage

admin.site.register(Woodwork)
admin.site.register(Like)
admin.site.register(Order)
admin.site.register(Rating)
admin.site.register(WoodworkImage)
