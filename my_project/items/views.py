from django.shortcuts import render,redirect
from .models import  FoundItem
from .forms import  FoundItemForm,LostSearchForm
from .utils import CATEGORY_MAP
import json
from django.utils.safestring import mark_safe
from datetime import datetime
# Create your views here.
def lost_search(request):
    form = LostSearchForm(request.GET or None)
    results = []
    
    if request.GET and form.is_valid():
        category = form.cleaned_data['category']
        location = form.cleaned_data['location']
        thing_name = form.cleaned_data.get('thing_name')
        search_date = form.cleaned_data.get('date')
        search_time = form.cleaned_data.get('time')


        if thing_name :
            results = FoundItem.objects.all()
        
            # Apply filters only if values are provided
            if category:
                results = results.filter(category=category)

            if location:
                results = results.filter(location=location)

            if thing_name:
                results = results.filter(title__icontains=thing_name)

            # Date filter
            
            if search_date and not search_time:
                results = results.filter(date_found__date=search_date)
                
            if search_time and not search_date:
                results = results.filter(date_found__time=search_time)
                
            if search_date and search_time:
                combined_datetime = datetime.combine(search_date, search_time)
                results = results.filter(date_found=combined_datetime)        
        else:
            results = []    
    category_map_json = mark_safe(json.dumps(CATEGORY_MAP))    
    return render(request, 'items/lost_search.html',{
        'form':form,
        'results':results,
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

          