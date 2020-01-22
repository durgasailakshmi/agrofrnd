from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'index.html')
def farmers(request):
	return render(request,'farmers.html')
def transportprovider(request):
	return render(request,'transportprovider.html')
def market(request):
	return render(request,'market.html')
def wearhouses(request):
	return render(request,'wearhouses.html')
def communityowner(request):
	return render(request,'communityowner.html')