#!/bin/bash -eum

pkill -f scrapyd
poetry run scrapyd &
sleep 1

(cd app/ && poetry run scrapyd-deploy)

fg %"poetry run scrapyd" >/dev/null
