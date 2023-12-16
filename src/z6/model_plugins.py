from uuid import uuid4

from model import *


class SimpleProblem(Problem):

    def render(self) -> bytes:
        # todo: wyświetlić ładnie pytanie na konsoli (razem z treściami odpowiedzi)
        console = ''
        console += '-' * 30 + '\n'
        console += self.problem_text + '\n\n'
        for q in self.questions:
            console += q.asked_text + '\n'
        console += '-' * 10 + '\n'
        return console.encode()

    @staticmethod
    def parse(text_lines: Iterable[str]) -> list['Problem']:
        # proper parse error exceptions (raises ParseError)
        """
        Whole test is given by a file with the following format:

        ```
        # duration_min, n_problems_per_test
        5 ;; 2
        ---
        TEXT: Następujące informacje nt. stolic są prawdziwe
        Q: Stolicą Rwandy jest Kigali ;; N ;; 2 ;; 0
        Q: Stolicą Irlandii jest Dublin ;; Y ;; 1 ;; -1

        ---
        TEXT: Następujące informacje nt. stolic są prawdziwe
        Q: Stolicą Rwandy jest Kigali ;; N ;; 2 ;; 0
        Q: Stolicą Irlandii jest Dublin ;; Y ;; 1 ;; -1

        ---
        TEXT: Następujące informacje nt. stolic są prawdziwe
        Q: Stolicą Rwandy jest Kigali ;; N ;; 2 ;; 0
        Q: Stolicą Irlandii jest Dublin ;; Y ;; 1 ;; -1

        # - linie zaczynajace się od # są komentarzami
        # - pierwsza linia to konfiguracja testu
        # - kolejne sekcje (oddzielone przez '---') są problemami (Problem)
        # - TEXT jest tekstem problemu
        # - linie zaczynające się od Q: to pytania
        # - każda z linii pytań zawiera, oddzielone przez ;; następujące dane:
        #     - tekst pytnia
        #     - czy należy na pytanie odpowiedzieć przez 'Y' czy 'N'
        #     - jaka jest wartosc poprawnej odpowiedzi
        #     - jaka jest wartosć niepoprawnej odpowiedzi
        ```

        """

        good_lines = []
        for ln in text_lines:
            ln = ln.strip()
            if ln.startswith('#'): continue
            if len(ln) == 0: continue
            good_lines.append(ln)

        lines = good_lines

        if not lines[0].startswith('---'):
            raise ValueError('first line incorrect (lacks ---)')

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

        return problems
