from celery import shared_task

from .utils import *
from .models import *

@shared_task
def process_hook_celery_task(request_id):
    try:
        hook_request = HookRequest.objects.get(pk=request_id)

        response = get_llm_response(hook_request.message)

        hook_request.update_response(response)
        requests.post(hook_request.callback_url, json=response)

    except Exception as e:
        print(e)
