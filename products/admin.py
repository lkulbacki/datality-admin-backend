from django.contrib import admin
from django.db.models.base import ModelBase

from . import models as products_models


class MultiDBModelAdmin(admin.ModelAdmin):
    '''
    A ModelAdmin special configuration to tell Admin to use alternative database 
    in offers app context.
    '''
    # A handy constant for the name of the alternate database.
    using = 'products'
    # to show ID field in admin
    readonly_fields = ('id',)

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'offers' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'offers' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'offers' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'offers' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'offers' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

for key, value in products_models.__dict__.items():
    if type(value) is ModelBase:
        admin.site.register(value, MultiDBModelAdmin)
