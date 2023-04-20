from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from .tasks import new_post_notify
from .models import PostCategory, Post
from  django.db.models.signals import post_save


# def send_notifications(preview, pk, tittle, subscribers):
#     html_content = render_to_string(
#         'post_created_email.html',
#         {
#             'text':preview,
#             'link':f'{settings.SITE_URL}/news/{pk}'
#         }
#     )
#
#     msg = EmailMultiAlternatives(
#         subject= tittle,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers,
#     )
#
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()

@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender,instance, **kwargs):
    if kwargs['action'] == 'post_add':
        new_post_notify.delay(instance.id)
        # categories = instance.postCategory.all()
        # subscribers_emails = []
        #
        # for cat in categories:
        #     subscribers = cat.subscribers.all()
        #     subscribers_emails += [s.email for s in subscribers]
        #
        # send_notifications(instance.preview(), instance.pk, instance.tittle, subscribers_emails)


# @receiver(post_save, sender=Post)
# def execute_task_on_post_save(sender, instance, created, **kwargs):
#     if created:
#         send_notify.delay(instance.id)

