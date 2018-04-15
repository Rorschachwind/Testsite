# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return render(request,'newpage/index.html')
#	return HttpResponse("Hello! You Have Created A New Page!")
