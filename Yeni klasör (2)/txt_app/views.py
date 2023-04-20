from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import CheckboxData


def my_view(request):
    if request.method == 'POST':
        selected_options = request.POST.getlist('selected_options')
        if True:
            data = CheckboxData()
            data.data = ','.join(selected_options)
            data.save()

        return redirect('/boxes/as')
    
    return render(request, 'txt_app/checkbox_form.html')



def my_view(request):
    if request.method == 'POST':
        selected_options = request.POST.getlist('options')
        
        data = CheckboxData()
        data.data = ','.join(selected_options)
        data.save()
    
    return render(request, 'txt_app/checkbox_form.html')



