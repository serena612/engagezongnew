# coding : utf-8

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

from django.conf import settings
from django.utils import timezone

__all__ = (
    "bg_scheduler",
    "with_scheduling",
)

bg_scheduler = BackgroundScheduler(
    jobstores={
        "default": RedisJobStore(
            jobs_key="background_scheduler_tasks",
            run_times_key="background_scheduler_running",
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT
        )
    },
    executors={
        "default": ThreadPoolExecutor(20),
        "processpool": ProcessPoolExecutor(5)
    },
    job_defaults={
        "coalesce": True,
        "misfire_grace_time": None,
        "max_instances": 1
    },
    timezone=timezone.utc
)


