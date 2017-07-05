from django.shortcuts import render_to_response
from .models import *

def index(request):
    index_text = 'enter the matrix'
    return render_to_response('index.html', {'index_text':index_text})

def info(request):
    info_text = 'info aye'
    return render_to_response('info.html', {'info_text':info_text})

def view_music(request):
    music_array = Music.objects.all()
    return render_to_response('info_music.html', {'music_array':music_array})

def view_group(request):
    groups_array = VkGroup.objects.all()
    return render_to_response('info_group.html', {"groups_array",groups_array})

def view_friend(request):
    friend_array = Friend.objects.all()
    return render_to_response('info_friend.html', {'friend_array',friend_array})

def view_note(request):
    note_array = Note.objects.all()
    return render_to_response('info_note.html', {'note_array':note_array})