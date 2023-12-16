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

    @staticmethod
    def parse(text_lines: Iterable[str]) -> 'Problem':
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

