import cmd
from parking_simulation import SocketClient

class Cli(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '> '
        with open("port.txt") as file:
            self.port = int(file.read())

    def do_quit(self, arg):
        print("\nbye bye")
        return 1

    def do_state(self, line):
        client = SocketClient(port=self.port)
        data = client.get_data()
        mess = "STATE: %s " % data.decode()
        print(mess)
        del client

    def emptyline(self):
        pass

    def run(self):
        self.cmdloop()

if __name__ == "__main__":
    cli = Cli()
    cli.run()
