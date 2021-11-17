"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730407005"


class Simpy:
    """Just a list to practice OOP."""

    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, vals: list[float]):
        """Constructor."""
        self.values = vals

    def __str__(self) -> str:
        """Returns Simpy in a string for people to read."""
        return f"{self.values}"

    def fill(self, filler: float, count: int) -> None:
        """Makes Simpy a list of filler repeated count times."""
        self.values = []
        i: int = 0
        while i < count:
            self.values.append(filler)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Makes Simpy a list of floats starting with start, ending before stop, incrementing by step."""
        self.values = []
        i: float = start
        assert step != 0.0

        if step > 0.0:
            while i < stop:
                self.values.append(i)
                i += step
        
        if step < 0.0:
            while i > stop:
                self.values.append(i)
                i += step
    
    def sum(self) -> float:
        """Adds up everything in self.values."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for addition."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            print("float")
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for exponentiation."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            print("float")
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return result

    def __eq__(self, vs: Union[float, Simpy]) -> list[bool]:
        """Returns mask checking whether every item in each Simpy is the same."""
        mask: list[bool] = []
        
        if isinstance(vs, float):
            for item in self.values:
                if item == vs:
                    mask.append(True)
                else:
                    mask.append(False)
        else:
            assert len(self.values) == len(vs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] == vs.values[i]:
                    mask.append(True)
                else:
                    mask.append(False)
                i += 1
        return mask

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checks whether items in self are greater than another Simpy or a float."""
        mask: list[bool] = []

        if isinstance(rhs, float):
            for i in self.values:
                if i > rhs:
                    mask.append(True)
                else:
                    mask.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    mask.append(True)
                else:
                    mask.append(False)
                i += 1
        return mask

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Returns value from simpy like list index or simpy of values based on mask."""
        result: Simpy = Simpy([])
        if isinstance(rhs, list):
            i: int = 0
            assert len(rhs) == len(self.values)
            while i < len(self.values):
                if rhs[i]:
                    result.values.append(self.values[i])
                i += 1
        else:
            return self.values[rhs]
        return result