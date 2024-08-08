from urllib import request
from django.http import Http404, HttpResponse, HttpResponseRedirect
import json
import os
from django.conf import settings
from django.shortcuts import redirect, render


def home(request):
    return render(request,"pages/index.html")

def images(request):
    return render(request,"pages/images.html")

def all_images(request):
    image_folder = os.path.join(settings.MEDIA_ROOT, 'images')
    if not os.path.exists(image_folder):
        return render(request,"not_found/404.html" , content_type="text/html")
    image_items = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f)) if f.lower().endswith(('.png','.jpg','.jpeg'))]
    if not image_items :
        return render(request,"not_found/content.html" , content_type="text/html")
    image_urls = [{'name':imaged, 'url':os.path.join(settings.MEDIA_URL, 'images', imaged)} for imaged in image_items]
    return render(request,"pages/all_images.html" , {'image_list':image_urls})


def all_pdf(request):
    pdf_folder = os.path.join(settings.MEDIA_ROOT, 'pdfs')
    if not os.path.exists(pdf_folder):
        return render(request,"not_found/404.html" , content_type="text/html")
    pdf_items = [p for p in os.listdir(pdf_folder) if os.path.isfile(os.path.join(pdf_folder, p)) if p.lower().endswith(('.pdf'))]
    if not pdf_items :
        return render(request,"not_found/content.html" , content_type="text/html")
    pdf_urls = [{'name':pdf, 'url':os.path.join(settings.MEDIA_URL, 'pdfs', pdf)} for pdf in pdf_items]
    return render(request,"pages/all_pdfs.html" , {'pdf_list':pdf_urls})

def all_music(request):
    music_folder = os.path.join(settings.MEDIA_ROOT, 'music')
    if not os.path.exists(music_folder):
        return render(request,"not_found/404.html" , content_type="text/html")
    music_items = [m for m in os.listdir(music_folder) if os.path.isfile(os.path.join(music_folder, m)) if m.lower().endswith(('.mp3'))]
    if not music_items :
        return render(request,"not_found/content.html" , content_type="text/html")
    music_urls = [{'name':music, 'url':os.path.join(settings.MEDIA_URL, 'music', music)} for music in music_items]
    return render(request,"pages/all_music.html" , {'music_list':music_urls})


def all_videos(request):
    videos_folder = os.path.join(settings.MEDIA_ROOT, 'videos')
    if not os.path.exists(videos_folder):
        return render(request,"not_found/404.html" , content_type="text/html")
    video_items = [v for v in os.listdir(videos_folder) if os.path.isfile(os.path.join(videos_folder, v)) if v.lower().endswith(('.mp4'))]
    if not video_items :
        return render(request,"not_found/content.html" , content_type="text/html")
    video_urls = [{'name':videos, 'url':os.path.join(settings.MEDIA_URL, 'videos', videos)} for videos in video_items]
    return render(request,"pages/all_videos.html" , {'video_list':video_urls})

# def download_image(request):
#     image_path = os.path.join("static","image.png")
#     with open(image_path, 'rb') as image_path:
#         image_content= image_path.read()
#     response = HttpResponse(image_content, content_type="image/png")
#     return response

def documents(request):
    return render(request,"pages/documents.html")

def csv_func(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="person.csv"'
    
    data = '''
            Name, Age, Gender
            Robert,22,Male
            Alice,19,femail

            '''
    response.write(data)
    return response

def download_pdf(request):
    pdf_path = os.path.join("media","the_story_of_the_boy.pdf")
    with open(pdf_path, 'rb') as pdf_file:
        pdf_content= pdf_file.read()
    response = HttpResponse(pdf_content, content_type="application/pdf")
    return response


def videos(request):
    return render(request,"pages/videos.html")

def download_video(request):
    video_path = os.path.join(settings.MEDIA_ROOT,"video.mp4")
    if not os.path.exists(video_path):
        raise Http404("Video file not found.")

    with open(video_path, 'rb') as video_path:
        video_content = video_path.read()
    response = HttpResponse(video_content, content_type="video/mp4")
    return response

def about(request):
    return HttpResponse('<h1 style="color:white; background:blue;">about us</h1>')

def contact_us(request):
    return render(request,"pages/contact.html")

def message(request):
    return HttpResponse('<h1 style="color:red;">message us page</h1>')

def download_video3(request):
    video_path = os.path.join(settings.MEDIA_ROOT,"video4.mp4")
    if not os.path.exists(video_path):
        return render(request,"not_found/404.html" , content_type="text/html")

    with open(video_path, 'rb') as video_path:
        video_content = video_path.read()
    response = HttpResponse(video_content, content_type="video/mp4")
    return response
