class Print:
    """Print messages sent to console"""
    def echo(self, message):
        print(message)

class Silent:
    """Drop messages sent to console"""
    def echo(self, message):
    	pass