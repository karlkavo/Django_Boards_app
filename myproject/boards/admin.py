"""
Author:     Karl Kavanagh
Date:       Jan 2019
Purpose:    manage permissions file

"""

from django.contrib import admin
from .models import Board

admin.site.register(Board)


# Register your models here.
