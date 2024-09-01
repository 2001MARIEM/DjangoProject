from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse , HttpResponseNotFound
from django.shortcuts import render
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
import gridfs
from bson import ObjectId

# Connexion à MongoDB
client = MongoClient('localhost', 27017)
db = client['imagedatabase']
fs = gridfs.GridFS(db)

def home(request):
    return HttpResponse('Hello')

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        print(request.FILES)  # Debug: Affiche les fichiers reçus
        if 'image' in request.FILES:
            image_file = request.FILES['image']
            
            # Stocker l'image dans GridFS
            file_id = fs.put(image_file, filename=image_file.name, timestamp=datetime.now())
            
            return JsonResponse({'message': 'Image uploaded successfully', 'file_id': str(file_id)}, status=201)
        else:
            return JsonResponse({'error': 'No image provided'}, status=400)
    else:
        return HttpResponseBadRequest('Only POST requests are allowed.')
    
def serve_image(request, file_id):
    try:
        image = fs.get(ObjectId(file_id))
        response = HttpResponse(image.read(), content_type="image/jpeg")
        response['Content-Disposition'] = f'inline; filename="{image.filename}"'
        return response
    except gridfs.errors.NoFile:
        return HttpResponseNotFound('File not found')
    except Exception as e:
        print(f"Error serving image: {e}")
        return HttpResponse(status=500)
  

def dashboard(request):
    latest_image = fs.find().sort("uploadDate", -1).limit(1)[0]
    return render(request, 'imageapp/dashboard.html', {'image_id': str(latest_image._id), 'image_filename': latest_image.filename})
