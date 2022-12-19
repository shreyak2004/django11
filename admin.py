from django.contrib import admin
from .models import student,faculty,message,reply,register

admin.site.register(student)
admin.site.register(faculty)
admin.site.register(message)
admin.site.register(reply)
admin.site.register(register)





class student(admin.ModelAdmin):


    list_display  = ['name']
    search_fields = ['name']

# admin.site.register(Country,CountryAdmin)




# class CityAdmin(admin.ModelAdmin):


#     list_per_page = 6

#     list_display  = ['name','population']
#     search_fields = ['name','population']

# admin.site.register(City,CityAdmin)


