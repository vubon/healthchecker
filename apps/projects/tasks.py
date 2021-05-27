import requests
from celery import shared_task

from apps.projects.models import Service


def update_status(service_id: int, response: requests.Response) -> None:
    """
    :param service_id
    :param response:
    :return:
    """
    print(service_id, response)
    if 200 <= response.status_code <= 299:
        Service.objects.filter(pk=service_id).update(status='ok')


@shared_task()
def fetch_data(*args, **kwargs):
    print(args, kwargs)
    for key, value in kwargs.items():
        try:
            res = requests.get(url=value)
            update_status(service_id=int(key), response=res)
        except (requests.ConnectionError, requests.Timeout) as err:
            print(err)
            return False
        except requests.HTTPError as err:
            print(err)
            return False
