from celery import shared_task
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from .models import Post, Category, PostCategory
from django.template.loader import render_to_string
import datetime




@shared_task
def my_task():
    #today = datetime.datetime.now()
    last_week = datetime.datetime.now() - datetime.timedelta(days=7)
    posts = Post.objects.filter(dateCreation__gte=last_week)
    print(f'{posts= }')
    categories = set(posts.values_list('postCategory__name', flat=True))
    print(f'{categories = }')
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))
    print(f'{subscribers = }')

    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts

        }
    )

    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body ='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def new_post_notify(instance_id):
    instance = Post.objects.get(pk=instance_id)
    categories = instance.postCategory.all()
    subscribers =[]

    for cat in categories:
        subscribers += cat.subscribers.all()

    subscribers = list(set(sub.email for sub in subscribers))
    print(subscribers)

    for mail in subscribers:
        html_content = render_to_string(
            'post_created_email.html',
            {
                'text': instance.preview,
                'link': f'{settings.SITE_URL}/news/{instance_id}'
            }
        )
        print(f'{mail = }')
        msg = EmailMultiAlternatives(
            subject=instance.tittle,
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[mail],
        )

        msg.attach_alternative(html_content, 'text/html')
        msg.send()
