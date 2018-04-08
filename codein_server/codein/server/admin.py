from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


#added user to admin.p

class MyUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password', 'developer','python', 'Java','C','Ruby','HTML','CSS','JavaScript', 'OtherLanguages',)}),
        (_('Personal info'), {'fields': ('email',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email')

#get_user_model points to our user model
admin.site.register(get_user_model(), MyUserAdmin)

