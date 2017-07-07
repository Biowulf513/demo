from django.shortcuts import render, render_to_response
from myforms.forms import MyNameForm
from django.http import HttpResponseRedirect

def my_name(request):
    if request.method == 'POST':
        form = MyNameForm(request.POST)

        if form.is_valid():
            return render (request, 'tranks.html', {'form':form})

    else:
        form = MyNameForm()

    return render(request, './forms.html', {'form':form})
