from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from complain.forms import ComplainForm
from django.contrib import messages
@csrf_protect
def complain(request):
    form = ComplainForm()
    if request.method == 'POST':
        form = ComplainForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your form has been submitted successfully!')
    context = {
        'form': form
    }
    return render(request, 'complain.html', context)