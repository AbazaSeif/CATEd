from django import template
from django.db.models import Sum

from monitoring.models import Worker

register = template.Library()

@register.inclusion_tag('monitoring/workers.html')
def get_pool_workers(user_pool):
    workers = Worker.objects.filter(address_pool=user_pool)
    return {'workers':workers}

@register.filter(name='pool_total_hash')
def pool_total_hash(user_pool):
    total = Worker.objects.filter(address_pool=user_pool).aggregate(Sum('reported_hash_rate'))['reported_hash_rate__sum']
    return total