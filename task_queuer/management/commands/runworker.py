from django.core.management.base import BaseCommand

from task_queuer import worker


class Command(BaseCommand):
    help = 'Runs the script that executes commands'

    def handle(self, *args, **options):
        worker.main()
        self.stdout.write(self.style.SUCCESS('Worker is now running'))
