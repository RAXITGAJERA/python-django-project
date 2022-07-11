from django.contrib import admin
from .models import signup, video ,videocommets

# Register your models here.
@admin.register(signup)
class signupAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_fullname', 'is_staff','block_unblock', 'password' )

@admin.register(video)
class videoAdmin(admin.ModelAdmin):
    list_display = ('Video_name', 'channel', 'Video_link','Country', 'City' )

@admin.register(videocommets)
class videocommetsAdmin(admin.ModelAdmin):
    list_display = ('sno', 'comment', 'timestamp','parent_id', 'post_id', 'user_id' )
