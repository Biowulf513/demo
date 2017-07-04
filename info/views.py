from django.shortcuts import render_to_response


def index(request):
    index_text = 'enter the matrix'
    return render_to_response('index.html', {'index_text':index_text})

def info(request):
    info_text = 'info aye'
    return render_to_response('info.html', {'info_text':info_text})
