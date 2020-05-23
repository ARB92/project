from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.forms import AuthenticationForm

class UserAdmin(AdminSite):
    login_form = AuthenticationForm

    def has_permission(self, request):
        """
        Removed check for is_staff.
        """
        return request.user.is_active
    # Anything we wish to add or override

user_admin_site = UserAdmin(name='usersadmin')
