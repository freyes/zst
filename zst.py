#!/usr/bin/python3

import sys
from pprint import pprint

import requests


ICON = {'SUCCESS': u"\u2713",
        'FAILURE': u"\u2718"}


class bcolors:
    SUCCESS = '\033[92m'
    FAILURE = '\033[91m'
    ENDC = '\033[0m'
    WARNING = '\033[93m'


def get_status():
    r = requests.get('http://zuul.openstack.org/status.json')
    return r.json()


def find_changes(status, change_id):
    changes = []
    for pipeline in status['pipelines']:
        for change in pipeline['change_queues']:
            for head in change['heads']:
                for x in head:
                  if x['id'].startswith(change_id):
                      changes.append(x)

    return changes


def job_print(job):
    result = job['result']
    name = job['name']
    print(getattr(bcolors, str(result), bcolors.WARNING),
          ICON.get(result, "-"),
          bcolors.ENDC, name, end='')

    if result == 'FAILURE':
        print(u" \u2192", job['report_url'])
    else:
        print('')


def main():
    change_id = sys.argv[1]

    status = get_status()
    changes = find_changes(status, change_id)

    for change in changes:
        for job in change['jobs']:
            job_print(job)


if __name__ == '__main__':
    main()
