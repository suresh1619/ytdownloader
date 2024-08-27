import os
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from yt_dlp import YoutubeDL

def youtube(request):
    message = None

    if request.method == 'POST':
        link = request.POST.get('video-url', '')
        target_folder = r'C:\Users\sures\Videos\videoes'  # Use raw string or double backslashes

        if link:
            # Create the target folder if it doesn't exist
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(target_folder, '%(title)s.%(ext)s'),  # Use os.path.join for cross-platform compatibility
            }

            try:
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])
                message = "Download completed successfully."
            except Exception as e:
                message = f"An error has occurred: {e}"
        return HttpResponseRedirect('thank/')

    # Render the form with any message
    return render(request, 'index.html', {'message': message})
def thank(request):
    return render(request,'thank.html')