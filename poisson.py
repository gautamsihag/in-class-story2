import time
import json
import sys
import numpy as np

rate = 2
while True:
	print (json.dumps({"t":time.time()}))
	sys.stdout.flush()
	#sys.stdout.flush()
	#delta_t = numpy.random.exponential(2)
	time.sleep(np.random.exponential(rate))

