from django.contrib import admin
from .models import User, UserProfile, Status, Category, Note


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")
    search_fields = ("name", "email")
    list_filter = ("name", "email")


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "birth_date")
    search_fields = ("user__name", "bio")
    list_filter = ("birth_date",)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_final")
    list_filter = ("is_final",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title", "description")
    list_filter = ("title",)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "status", "created_at")
    search_fields = ("text", "author__name", "status__name")
    list_filter = ("status", "categories", "created_at")
    filter_horizontal = ("categories",)
