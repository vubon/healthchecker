from celery import shared_task

from apps.cores.resource_info import SystemHealthChecker
from apps.system.models import System


@shared_task()
def system_service_health(*args, **kwargs):
    h = SystemHealthChecker()
    redis = h.get_redis()
    workers = h.get_celery()

    redis_obj = System.objects.filter(name__iexact=redis.name)
    if redis_obj.exists():
        redis_obj.update(**{"status": redis.status, "config": redis.config})
    else:
        System.objects.create(name=redis.name, service_name="Redis", status=redis.status, config=redis.config)

    workers_obj = System.objects.filter(service_name__iexact="Celery")

    active_worker = workers_obj.filter(name__in=workers)
    not_active = workers_obj.exclude(name__in=workers)
    if active_worker.exists():
        active_worker.update(**{"status": True})
    if not_active.exists():
        not_active.update(**{"status": False})
    else:
        for worker in workers:
            if not workers_obj.filter(name__iexact=worker).exists():
                System.objects.create(status=True, name=worker, service_name="Celery")

    if not workers:
        workers_obj = System.objects.filter(service_name__iexact="Celery")
        workers_obj.update(**{"status": False})

    return True
