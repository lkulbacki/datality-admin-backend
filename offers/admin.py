from django.contrib import admin
from datality_admin.multidb_admin_base import MultiDBModelAdmin
from .models import Offer, Price, EntriesCrs


class OffersModelAdmin(MultiDBModelAdmin):
    using = 'offers'

admin.site.register(Offer, OffersModelAdmin)
admin.site.register(Price, OffersModelAdmin)
admin.site.register(EntriesCrs, OffersModelAdmin)
