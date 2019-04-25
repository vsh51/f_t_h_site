from django.shortcuts import render



def home_render(request):
    return render(request, 'home/home_page.html')

def about_us_render(request):
    return render(request, 'home/about_us.html')

def riddles_render(request):
    return render(request, 'home/riddle_render.html')

def sketches_render(request):
    return render(request, 'home/skeatch_render.html')

def join_render(request):
    return render(request, 'home/join_render.html')
