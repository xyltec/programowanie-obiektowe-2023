from model import *
from model_plugins import *


class ExamDriver:

    def __init__(self):
        self.test = None

    def load_test(self, file_name: str, problem_class: type):
        # todo: the `selected_class` should extend Problem
        # parse exam config
        with open(file_name, 'r') as f:
            lines = f.readlines()

        problems = SimpleProblem.parse(lines)

        # now -- parse the list of problems from file_name, all parsed to the selected problem_class

    def run_test(self):
        pass


if __name__ == '__main__':
    e = ExamDriver()
    pp = e.load_test('simple_problem_exam_exmple.txt', SimpleProblem)
    for p in pp:
        print(p)



