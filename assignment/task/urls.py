from django.urls import path, include
from django.conf import settings
from .views import home,images,documents,videos, message, about, contact_us, csv_func,download_pdf,download_video,download_video3,all_images,all_pdf,all_music,all_videos


urlpatterns = [
     path('',home, name="index"),
     path('images',images, name="images"),
     path('documents',documents, name="documents"),
     path('videos',videos),
     path('message', message, name="message"),
     path('about', about, name="about"),
     path('contact', contact_us, name="contact"),
     path('csv', csv_func, name="csv"),
     path('download_pdf', download_pdf, name="pdf"),
     # path('images',download_image, name="image"),
     path("video",download_video, name="video"),
     path("video3",download_video3, name="video3"),
     path("all-pdfs",all_pdf, name="all-pdfs"),
     path("all-images",all_images, name="all_images"),
     path("all-music",all_music, name="all-music"),
     path("all-videos",all_videos, name="all-videos"),
     path("__reload__/", include("django_browser_reload.urls")),
]
