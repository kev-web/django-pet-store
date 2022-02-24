#django-import-export imports:
from import_export import resources
from import_export.admin import ImportExportModelAdmin
#Default Django imports
from django.contrib import admin
#My simbapp imports:
from .models import CodingPics, DogInfo




#django-import-export
#Create a class:
class DogInfoResource(resources.ModelResource):
    class Meta:
        model = DogInfo


class DogInfoAdmin(ImportExportModelAdmin):
    resource_class = DogInfoResource




admin.site.register(CodingPics)
admin.site.register(DogInfo, DogInfoAdmin)







