#!/bin/bash
gunicorn --config gunicorn-cfg.py core.wsgi
