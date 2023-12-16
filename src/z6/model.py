from collections.abc import Iterable
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Question:
    asked_text: str
    correct_value: int
    incorrect_value: int
    answer_should_be_true: bool  # answer Y is correct


@dataclass
class Problem:
    problem_id: UUID
    questions: list[Question]
    problem_text: str

    def render(self) -> bytes:
        # displayed to test taker
        pass

    def parse(self, text_lines: Iterable[str]) -> 'Problem':
        # proper parse error exceptions (raises ParseError)
        pass


class ParseError(ValueError):
    pass


@dataclass
class SubmittedProblemAnswer:
    answer_id: UUID
    problem_id: UUID
    user_id: UUID
    permutation: list[int]  # order in which questions were displayed to user
    ticked_correct: list[bool]
    scored_points: int


class ExamConfig:
    duration: float
    n_questions: int


@dataclass
class ExamInstance:
    problems: list[Problem]
    answers: list[SubmittedProblemAnswer]
    final_score: int
    created_at: datetime
    finished_at: datetime


class ExamDriver:

    def load_test(self, file_name: str, problem_class: type):
        # todo: the `selected_class` should extend Problem
        # parse exam config

        problems = []
        # now -- parse the list of problems from file_name, all parsed to the selected problem_class

    def run_test(self):
        pass

# process of asking question:
# - system loads problems, selects the list asked to user
# - for each problem system creates a random permutation (order in which questions are displayed),
#   and saves the "blank" SubmittedProblemAnswer somewhere (memory)
# - user sends "list[bool]" (his answers); system computes score, and updates SubmittedProblemAnswer
#
