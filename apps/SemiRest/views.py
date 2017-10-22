# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from .models import *
from django.contrib import messages

def index(request):
    context = {}
    context['stuff'] = User.objects.all()
    
    return render(request,'SemiRest/index.html',context)

def show(request, number):
    context = {}
    context['stuff'] = User.objects.get(id = number)
    
    return render(request,'SemiRest/users.html',context)

def edit(request, number):
    context = {}
    context['stuff'] = User.objects.get(id = number)
    
    return render(request,'SemiRest/edit.html',context)

def update(request,number):
    first = request.POST['first']
    last = request.POST['last']
    email = request.POST['email']
    x = {'first': first,'last': last, 'email': email}
    errors = User.objects.validate(x)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/{}/edit'.format(number))
    else:
        user = User.objects.get(id = number)
        user.first = request.POST['first']
        user.last = request.POST['last']
        user.email = request.POST['email']
        user.save()
        return redirect('/')

def new(request):
    
    return render(request,'SemiRest/new.html')

def addUser(request):
    print request.POST
    first = request.POST['first']
    last = request.POST['last']
    email = request.POST['email']
    x = {'first': first,'last': last, 'email': email}
    errors = User.objects.validate(x)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/new')
    else:
        
        user = User.objects.create(first = first, last = last, email = email )
        print User.objects.all()
        return redirect('/')

def delete(request, number):
    x = User.objects.get(id=number)
    x.delete()
    
    
    return redirect('/')

