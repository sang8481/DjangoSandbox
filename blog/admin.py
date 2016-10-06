from django.contrib import admin
from .models import Post

## Let server knows about our application.
admin.site.register(Post)
