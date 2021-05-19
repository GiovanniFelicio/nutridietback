from django.contrib import admin

from core.common.models import User
from person.models.person import Person


admin.site.register(Person)
admin.site.register(User)
# Register your models here.
