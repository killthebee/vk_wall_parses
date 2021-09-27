import vk_api
import re
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from wordcloud import WordCloud
from io import BytesIO
from django.core.files.base import ContentFile
from vk_api.exceptions import ApiError

from vk_parser import models


class ParseView(APIView):
    def get(self, request, **kwargs):
        wall_url = kwargs.get('wall_url')
        vk_login = os.environ.get('vk_login')
        vk_password = os.environ.get('vk_password')
        vk_session = vk_api.VkApi(login=vk_login, password=vk_password)
        vk_session.auth()
        vk = vk_session.get_api()
        try:
            if wall_url.startswith('club'):
                posts = vk.wall.get(
                    owner_id=f'-{wall_url[4:]}',
                )['items']
            elif wall_url.startswith('public'):
                posts = vk.wall.get(
                    owner_id=f'-{wall_url[6:]}',
                )['items']
            else:
                posts = vk.wall.get(
                    domain=wall_url,
                )['items']
        except ApiError:
            return Response({'success': False, 'words': {}})
        try:
            posts_data = [
                {'id': post['id'], 'likes': post['likes']['count'], 'views': post['views']['count']} for post in posts
            ]
        except KeyError:
            posts_data = [
                {'id': post['id'], 'likes': post['likes']['count'], 'views': 'unknown'} for post in posts
            ]
        all_texts = ""
        for post in posts:
            try:
                all_texts = all_texts + " " + post["text"]
            except TypeError:
                continue
        words = ' '.join(re.findall(r"[а-яА-Я]+", all_texts))
        try:
            wordcloud = WordCloud(max_font_size=40).generate(words)
        except ValueError:
            return Response({'success': False, 'words': {}})
        image = wordcloud.to_image()
        image_io = BytesIO()
        image.save(image_io, format='jpeg', quality=80)
        instance, created = models.ParseResults.objects.get_or_create(submission=wall_url)
        instance.image.save(f'image_for_{wall_url}.jpeg', ContentFile(image_io.getvalue()))
        instance.posts_data = posts_data
        instance.save()
        return Response({'success': True, 'words': words})
