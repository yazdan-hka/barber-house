from django.shortcuts import render

# Create your views here.

def nft(request):
    return render(request, 'nft.html')

