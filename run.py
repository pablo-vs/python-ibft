import argparse
from flask import json
import threading
import python_ibft as ibft

parser = argparse.ArgumentParser(description='Run Istanbul BFT process.')
parser.add_argument('process_id', metavar='process_id', type=int, 
                    help='The ID of the process')
parser.add_argument('--parties', metavar='parties_json', type=str, default="conf/parties.json",
                    help='JSON configuring the parties')
parser.add_argument('--config', metavar='config_json', type=str, default="conf/config.json",
                    help='JSON configuration')
parser.add_argument('--privkey', metavar='privkey_json', type=str, default="",
                    help='JSON configuration')
parser.add_argument('--input-value', metavar='input_value', type=str, default="",
                    help='Use as input value')
parser.add_argument('--test-validity', metavar='validity', type=str, default="",
                    help='Consider all values different from the given one as invalid')
parser.add_argument("--offline",dest='offline',action='store_true', help="Defect mode: this process is offline.")
parser.add_argument("--random-values",dest='random_values',action='store_true', help="Defect mode: this process will send random values in messages.")
parser.add_argument("--online-delayed",dest='online_delayed',action='store_true', help="Defect mode: Only come online after 60 seconds.")
parser.add_argument("--offline-delayed",dest='offline_delayed',action='store_true', help="Defect mode: Go offline after 60 seconds.")
parser.add_argument("--offline-after-prepare",dest='offline_after_prepare',action='store_true', help="Defect mode: Go offline after first round is prepared.")

args = parser.parse_args()

ibft_id = args.process_id
print("I am IBFT process {0}".format(ibft_id))

if args.online_delayed:
    print("Waiting 60s to go online")
    time.sleep(60)
    print("Now online")

if args.offline_delayed:
    print("Will go offline after 60s")
    def go_offline():
        print("Going offline")
        os._exit(0)

    threading.Timer(60, go_offline).start()

if args.privkey == "":
    privkey_file = "conf/privkey_{0}.json".format(ibft_id)
else:
    privkey_file = args.privkey

if args.test_validity != "":
    valid = lambda x: x == args.test_validity
else:
    valid = None

privkey_json = json.load(open(privkey_file, "r"))
parties_json = json.load(open(args.parties, "r"))
config_json = json.load(open(args.config, "r"))

if not args.offline:
    ibft.start_ibft(privkey_json, parties_json, config_json, ibft_id)
    ibft.start_instance(0, args.input_value, validity_callback=valid)
else:
    print("I'm offline, doing nothing")
    input()
