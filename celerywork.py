#!/usr/bin/env python

from app.utils.tsk import celery
from app import create_app

app = create_app()
app.app_context().push()