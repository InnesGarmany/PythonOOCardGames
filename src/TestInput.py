from input import Input
class TestInput(Input):
    test_inputs = []

    def set_test_inputs(self, inputs):
        self.test_inputs = inputs

    def get_input(self, message):
        return self.test_inputs.pop()
