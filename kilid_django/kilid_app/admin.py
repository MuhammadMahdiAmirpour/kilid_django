from django.contrib import admin
from kilid_app.models import Province, Region, City, AgencyManager, EstateAgency, AgencyAdvisor, House, Advertisement

# Register your models here.
admin.site.register(Province)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(AgencyAdvisor)
admin.site.register(EstateAgency)
admin.site.register(AgencyManager)
admin.site.register(House)
admin.site.register(Advertisement)
