from django.shortcuts import render,redirect
from .models import LostItem, FoundItem
from .forms import LostItemForm, FoundItemForm,LostSearchForm
from .utils import matches_category_keywords,CATEGORY_MAP
import json
from django.utils.safestring import mark_safe
# Create your views here.
def lost_search(request):
    form = LostSearchForm(request.GET or None)
    results = []
    
    if form.is_valid():
        category = form.cleaned_data['category']
        location = form.cleaned_data['location']
        thing_name = form.cleaned_data.get('thing_name')
        date_time = form.cleaned_data.get('date_time')
        
        lost_items = LostItem.objects.filter(category=category, location=location )
        found_items = FoundItem.objects.filter(category=category, location=location )
        
        if thing_name:
            lost_items = lost_items.filter(title__icontains = thing_name)
            found_items = found_items.filter(title__icontains=thing_name)
            
        if date_time:
            lost_items = lost_items.filter(date_time__gte=date_time)
            found_items = found_items.filter(date_time__gte=date_time)        
            
        results = list(lost_items) + list(found_items)  
    category_map_json = mark_safe(json.dumps(CATEGORY_MAP))    
    return render(request, 'items/lost_search.html',{
        'form':form,
        'results':results,
        'category_map_json': category_map_json,
    })      

def lost_view(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LostItemForm()
    category_map_json = mark_safe(json.dumps(CATEGORY_MAP))      
    return render(request, 'items/lost_form.html',{
        'form':form,
        'category_map_json': category_map_json,
        })


def found_view(request):
    if request.method == 'POST':
        form = FoundItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = FoundItemForm() 
    category_map_json = mark_safe(json.dumps(CATEGORY_MAP))   
    return render(request, 'items/found_form.html',{
        'form':form,
        'category_map_json': category_map_json,
        })   

          