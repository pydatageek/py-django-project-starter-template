from django.contrib import admin

from .models import User, Group, DjangoGroup

admin.site.unregister(DjangoGroup)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass
