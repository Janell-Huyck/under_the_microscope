from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from my_user.models import MyUser
from my_user.forms import MyUserForm, MyUserChangeForm

# help in this section is from https: // testdriven.io/blog/django-custom-user-model/


class MyUserAdmin(UserAdmin):
    list_display = ('username', 'display_name', 'home_page',
                    'age', 'is_staff', 'is_active',)
    list_filter = ('username', 'display_name', 'home_page',
                   'age', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'display_name', 'home_page', 'age')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )


admin.site.register(MyUser, MyUserAdmin)
