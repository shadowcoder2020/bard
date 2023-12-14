from doh      import Query
from time      import sleep
from threading import Thread, Lock

class DnsCache:
	def __init__(self, server_name, delay):
		self.lock             = Lock()
		self.delay            = delay
		self.address          = Query(server_name)
		self.server_name      = server_name

		Thread(target=self.update).start()

	def update(self):
		while True:
			response = Query(self.server_name)
			if response:
				with self.lock:
					self.address = response

			sleep(self.delay)

	@property
	def getaddress(self):
		return self.address