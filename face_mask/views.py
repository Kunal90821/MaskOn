from django.shortcuts import render
from .training import without_mask_data
from .training import with_mask_data
from .detection import mask_face

# Create your views here.

def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def training_without_mask(request):
	train_data_without_mask = without_mask_data()
	return render(request,'index.html')

def training_with_mask(request):
	train_data_without_mask = with_mask_data()
	return render(request,'index.html')

def contact(request):
	return render(request,'contact.html')

def detection(request):
	detection_face = mask_face()
	return render(request,'index.html')