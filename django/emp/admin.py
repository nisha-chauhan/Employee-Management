from django.contrib import admin
from .models import Emp,Testimonial
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=('emp_id','name','phone', 'working','department')
    list_editable=('name','phone', 'working','department')
    search_fields=('name',)
    
    
admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)