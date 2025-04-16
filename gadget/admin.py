from django.contrib import admin
from gadget.models import Gadgets

#For better View
class GadgetsAdmin(admin.ModelAdmin):
    list_display = ('id','model','category', 'picture','price','about','agree','upload_time','update_time')

# Register your models here.
admin.site.register(Gadgets,GadgetsAdmin)