import subprocess
from django.shortcuts import render_to_response
from django.http import HttpResponse


def home(request):
    return render_to_response("index.html")


def rabuissao(request):
    output = subprocess.check_output(["rabuissa.o"])
    return HttpResponse(output)


def proc(request):
    return render_to_response("rabuissa_proc_fun.txt")


def server(request):
    return render_to_response("server.html")
