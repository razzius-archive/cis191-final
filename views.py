import os
from django.shortcuts import render_to_response
from django.http import HttpResponse


def home(request):
    return render_to_response("index.html")


def rabuissao(request):
    output = os.system("/home/ubuntu/cis191-final/wrapper.sh")
    output = output[:-1]  # the 0 output status is extraneous
    return HttpResponse(output)


def proc(request):
    return render_to_response("rabuissa_proc_fun.txt")


def server(request):
    return render_to_response("server.html")
