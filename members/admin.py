from django.contrib import admin

# Register your models here.

from .models import Members
# Register your models here.

class MembersAdmin(admin.ModelAdmin):
    list_display = ('username','useremail')
    pass

admin.site.register(Members, MembersAdmin)
