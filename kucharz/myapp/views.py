from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
# Create your views here.


from myapp.forms import LogForm

@csrf_protect
def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, 'home.html', context)