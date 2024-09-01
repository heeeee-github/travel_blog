from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def get_first_image(post):
    first_image = post.images.first()
    if first_image:
        return first_image.image.url
    return f"{settings.STATIC_URL}blog/images/default_thumbnail.jpg"