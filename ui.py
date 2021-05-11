import argparse
import os
import subprocess
import sys

import psutil
import simplejson as json
import simplejson.errors
from mss import mss
from screeninfo import get_monitors

from api import Api

more_indent_formatter = lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position=35)
parser = argparse.ArgumentParser(description="Configure your devlights as ambilight",
                                 formatter_class=more_indent_formatter, add_help=False)

monitors = get_monitors()
indexes = [index for index, value in enumerate(monitors)]
api = Api()
sct = mss()
path = os.path.expanduser("~") + "/.ambidevlight/data.json"
if not os.path.exists(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "x")

defaults = {"width": 16, "height": 9, "index": 0}
try:
    with open(path, "r") as file:
        defaults = json.load(file)
except simplejson.errors.JSONDecodeError as err:
    pass

parser.add_argument("-w", "--horizontal", type=int, default=defaults.get("width"), dest="width",
                    help="horizontal LED count")
parser.add_argument("-h", "--vertical", type=int, default=defaults.get("height"), dest="height",
                    help="vertical LED count")
parser.add_argument("-m", "--monitor", type=int, dest="index", default=defaults.get("index"),
                    choices=indexes, help="monitor strip is attached to")
parser.add_argument("--help", action="help", help="show this help message")
parser.add_argument("-l", "--list", dest="list", action="store_true", help="list available monitors")
args = parser.parse_args()

if args.list:
    for index, mon in enumerate(monitors):
        print("\t{}. '{}'\t({}x{})".format(index, mon.name, mon.width, mon.height).expandtabs(5))
    exit(0)

with open(path, "w") as file:
    json.dump(vars(args), file)

start_message = "Starting ambilight on monitor '{}' ({}x{}) with {}x{} LEDs."
mon = monitors[args.index]
print(start_message.format(mon.name, mon.width, mon.height, args.width, args.height))
proc_iter = psutil.process_iter(attrs=["pid", "name", "cmdline"])
for p in proc_iter:
    if "ambidevlight_bg_run.py" in p.cmdline():
        print("Found old running instance. Killing it! (Multiple screens/lights are not supported at the time)")
        p.kill()
log = open("run.log", "w+")
p = subprocess.Popen(
    [sys.executable, 'ambidevlight_bg_run.py', str(args.index), str(args.width), str(args.height)],
    stdout=log,
    stderr=subprocess.STDOUT)

print("To stop it run 'kill {}'".format(p.pid))
