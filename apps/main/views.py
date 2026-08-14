import os
from django.shortcuts import render
from django.conf import settings

def home(request):
    # Get partner images from static/images/partners/
    partners_dir = os.path.join(settings.BASE_DIR, 'static', 'images', 'partners')
    partner_images = []
    if os.path.exists(partners_dir):
        for filename in sorted(os.listdir(partners_dir)):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.svg', '.webp')):
                partner_images.append({
                    'name': os.path.splitext(filename)[0].replace('_', ' ').title(),
                    'image': f'images/partners/{filename}',
                })
    return render(request, 'home.html', {'partner_images': partner_images})
