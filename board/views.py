from django.views.generic import TemplateView, ListView, DetailView

from .models import SoundBoard

class IndexView(TemplateView):
    """
    Temp home page
    """
    template_name = 'index.html'

class BoardListView(ListView):
    """
    Shows SoundBoard listing
    """
    model = SoundBoard
    template_name = 'board-list.html'

class BoardDetailView(DetailView):
    """
    Shows SoundBoard detail, e.g. the soundboard itself
    """
    model = SoundBoard
    template_name = 'board-detail.html'
