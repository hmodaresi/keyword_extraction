from django.conf.urls import url

from text_parser import views
urlpatterns = [
    url(r'add_article', views.add_article, name='add_article'),
    url(r'get_keywords', views.get_keywords, name='get_keywords'),
    url(r'new_game', views.new_game, name='new_game'),
    url(r'get_containing_sentences', views.get_containing_sentences, name='get_containing_sentences'),
    url(r'get_containing_paragraphs', views.get_containing_paragraphs, name='get_containing_paragraphs'),
    url(r'get_completed_sentence', views.get_completed_sentence, name='get_completed_sentence'),
    url(r'is_sentence_complete', views.is_sentence_complete, name='is_sentence_complete'),
    url(r'get_topics', views.get_topics, name='get_topics'),
    url(r'add_site', views.add_site, name='add_site'),
    url(r'get_sites', views.get_sites, name='get_sites')

]

