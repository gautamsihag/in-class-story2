import json
import sys

last = 0
while True:
	line = sys.stdin.readline()
	d = json.loads(line)
	
	if last == 0:
		last = d["t"]
		continue
	delta = d["t"] - last
	print (json.dumps({"t":d["t"], "delta": delta}))
	sys.stdout.flush()
	last = d["t"]

