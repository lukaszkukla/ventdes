from django.shortcuts import render


def privacy(request):
    """A view to return privacy policy"""
    return render(request, 'policy/privacy.html')
