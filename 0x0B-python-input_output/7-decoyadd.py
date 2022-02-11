import sys

save_from_json_file = __import__('5-save_from_json_file').save_from_js0n_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
try:
    listt = load_from_json_file("add_item.json")
except:
    listt = []

argcount = len(sys.argv) - 1

if argcount > 0:
    for item in (argcount):
        listt.append(sys.argv[item])

save_from_json_file(listt, "add_item.json")
