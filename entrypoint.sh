#!/bin/bash

aerich upgrade
uvicorn main:app --reload --host 0.0.0.0 --root-path /api --port 8000
