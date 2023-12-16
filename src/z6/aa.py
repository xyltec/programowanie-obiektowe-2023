from uuid import uuid4

from src.z6.model import Question
from src.z6.model_plugins import SimpleProblem

if __name__ == '__main__':
    with open('simple_problem_exam_example.txt', 'r') as f:
        lines = f.readlines()

    good_lines = []
    for ln in lines:
        ln = ln.strip()
        if ln.startswith('#'): continue
        if len(ln) == 0: continue
        good_lines.append(ln)

    lines = good_lines

    if not lines[1].startswith('---'):
        raise ValueError('file lacks first --- line')

    problems = []
    questions = []
    problem_text = ''
    for ln in lines[2:]:
        if ln.startswith('---'):
            p = SimpleProblem(uuid4(), questions, problem_text)
            problems.append(p)
            # create Question
            questions = []
        elif ln.startswith('TEXT:'):
            problem_text = (ln[5:]).strip()
        elif ln.startswith('Q:'):
            zz = (ln[2:]).strip().split(';;')
            text_ = zz[0]
            y_n = zz[1].strip()
            correct_value = int(zz[2])
            incorrect_value = int(zz[3])
            q = Question(text_, correct_value, incorrect_value, y_n == 'Y')
            questions.append(q)
        else:
            raise ValueError('wrong format in problem section')

    # parse exam config (this is the first line)
    # then expect '---'
    # then parse problem text
    # then parse quenstion's until the line with `---` is encountered ....

    for p in problems:
        print(p)