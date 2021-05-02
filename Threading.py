import threading

class messanger(threading.Thread):
	def run(self):
		for _ in range(10):
			print(threading.currentThread().getName())

x = messanger(name = 'Send out messages')
y = messanger(name = 'Receive messages')

x.start()
y.start()