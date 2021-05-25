from django.contrib import admin
from datality_admin.multidb_admin_base import MultiDBModelAdmin
from django.db.models.base import ModelBase

from . import models as products_models


class ProductModelAdmin(MultiDBModelAdmin):
    using = 'products'

for key, value in products_models.__dict__.items():
    if type(value) is ModelBase:
        admin.site.register(value, ProductModelAdmin)
