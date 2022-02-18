from django.contrib import admin

from .forms import DocumentAdminForm
from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'visible')
    list_filter = ('visible',)
    date_hierarchy = 'created'
    form = DocumentAdminForm
