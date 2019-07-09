from django.contrib import admin
from .models import Post


class TutorialAdmin(admin.ModelAdmin):
    fields = ["title",
              "published_time",
              "content",
              "author"]


admin.site.register(Post)
