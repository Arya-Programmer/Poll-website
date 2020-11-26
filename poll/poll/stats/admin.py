from django.contrib import admin
from .models import Stat

# Register your models here.


class AdminStat(admin.ModelAdmin):
    # readonly_fields = ('ip', 'is_valid', 'answers', 'poll_id')
    pass

admin.site.register(Stat, AdminStat)