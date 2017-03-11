import time
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from functools import partial
from subprocess import check_call

from django.utils import timezone

from task_queuer.models import Task


def get_tasks_ids():
    min_interval = 1
    while True:
        start_time = time.time()
        t = Task.objects.values_list('id', flat=True).filter(start_time=None)
        yield from t
        spent_time = time.time() - start_time
        if spent_time < min_interval:
            time.sleep(min_interval - spent_time)


def run_task():
    check_call("task_queuer/test_task.py")


def finish_task(task_id, future):
    future.result()
    Task.objects.filter(id=task_id).update(finish_time=timezone.now())


def main():
    max_concurrency = 2
    done, not_done, running = set(), set(), set()
    task_id_generator = get_tasks_ids()
    with ThreadPoolExecutor(max_concurrency) as executor:
        while True:
            if len(not_done) < max_concurrency:
                task_id = next(task_id_generator)
                Task.objects.filter(id=task_id).update(start_time=timezone.now())
                task = executor.submit(run_task)
                running.add(task)
                callback = partial(finish_task, task_id)
                task.add_done_callback(callback)
            done, not_done = wait(running, return_when=FIRST_COMPLETED, timeout=1)
            running -= done

if __name__ == '__main__':
    main()
