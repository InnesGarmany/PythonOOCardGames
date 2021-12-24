from output import Output
class ConsoleOutput(Output):

    def output(self, message, endChar = "\n"):
        print(message, end = endChar)