from input import Input 
class ConsoleInput(Input):

    def get_input(self,message):
        return input(message)