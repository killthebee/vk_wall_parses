from django.views import generic

from vk_parser import models


class MainView(generic.TemplateView):
    template_name = 'main.html'
    model = models.ParseResults

    def get_context_data(self, **kwargs):
        obj = self.model.objects.all().last()
        try:
            return {'request': obj.submission, 'image': obj.image.url, 'posts_data': obj.posts_data}
        except AttributeError:
            return {'request': '', 'image': ''}
