from collections.abc import Iterable
from dataclasses import dataclass
from uuid import UUID


@dataclass
class Question:
    asked_text: str
    correct_value: int
    incorrect_value: int
    answer_is_correct: bool


@dataclass
class Problem:
    problem_id: UUID
    questions: list[Question]

    def render(self) -> bytes:
        pass

    def parse(self, text_lines: Iterable[str]) -> 'Problem':
        pass


@dataclass
class ProblemAnswer:
    answer_id: UUID
    problem_id: UUID
    user_id: UUID
    permutation: list[int]  # order in which questions were displayed to user
    ticked_correct: list[bool]
    scored_points: int


# process of asking question:
# - system loads problems, selects the list asked to user
# - for each problem system creates a random permutation (order in which questions are displayed),
#   and saves the "blank" ProblemAnswer somewhere (memory)
# - user sends "list[bool]" (his answers); system computes score, and updates ProblemAnswer
#
