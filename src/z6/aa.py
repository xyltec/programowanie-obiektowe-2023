if __name__ == '__main__':
    with open('simple_problem_exam_example.txt', 'r') as f:
        lines = f.readlines()

    for ln in lines:
        ln = ln.strip()
        if ln.startswith('#'): continue
        if len(ln) == 0: continue
        print(ln)

    # parse exam config (this is the first line)
    # then expect '---'
    # then parse problem text
    # then parse quenstion's until the line with `---` is encountered ....