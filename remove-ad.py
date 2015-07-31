#!/usr/bin/env python3
from json import loads, dumps
from os.path import dirname, realpath, join
from os import chdir
from sys import argv
from subprocess import call

SCRIPT_PATH = dirname(realpath(__file__))
JSON_NAME = "owned-sku.json"
JSON_PATH = join(SCRIPT_PATH, JSON_NAME)
SKU_NAME = "ad_removal"

if __name__ == "__main__":
  data = loads(open(JSON_PATH).read())
  if len(argv) == 2:
    data[SKU_NAME].append(int(argv[1]))
  data[SKU_NAME].sort()
  with open(JSON_PATH, "w") as file:
    file.write(dumps(data))
  chdir(SCRIPT_PATH)
  call(["git", "add", JSON_NAME])
  call(["git", "commit", "-m", "Added user ID"])
  call(["git", "push", "origin", "master"])
