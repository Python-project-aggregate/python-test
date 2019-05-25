class Command:
    def __init__(self):
        self.cmd = {}

    def com(self):
        while True:
            num = input('>>')
            if num == 'quit':
                break
            if num in self.cmd:
                print( self.cmd[num])
            else:
                self.cmd.get(0)


Command().com()