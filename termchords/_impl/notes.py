import enum
from typing import Dict, Set, Tuple


class Accidental(enum.Enum):
    Natural = enum.auto()
    Sharp = enum.auto()
    Flat = enum.auto()

    def to_str(self) -> str:
        if self == Accidental.Natural:
            return ""
        elif self == Accidental.Sharp:
            return "#"
        elif self == Accidental.Flat:
            return "b"
        raise ValueError(str(self))


def notes() -> Dict[int, "_Note"]:
    if not _Note._all_notes:
        # Create all notes.
        for octave in range(8):
            for i in range(7):
                note_chr = chr(ord("A") + i)
                _ = _Note(octave, note_chr)

                # Add sharps and flats.
                _ = _Note(octave, note_chr, Accidental.Sharp)
                _ = _Note(octave, note_chr, Accidental.Flat)

    return _Note._all_notes


class _Note:
    """Represents a cached note.

    Each note is assigned a number starting from C0. Notes with
    accidentals will share the same number.
    """

    _all_notes: Dict[Tuple[int, int, Accidental], "_Note"] = {}
    _by_num: Dict[int, Set["_Note"]] = {}

    _rel = {
        ("C", Accidental.Flat): -1,
        ("C", Accidental.Natural): 0,
        ("C", Accidental.Sharp): 1,
        ("D", Accidental.Flat): 1,
        ("D", Accidental.Natural): 2,
        ("D", Accidental.Sharp): 3,
        ("E", Accidental.Flat): 3,
        ("E", Accidental.Natural): 4,
        ("E", Accidental.Sharp): 5,
        ("F", Accidental.Flat): 4,
        ("F", Accidental.Natural): 5,
        ("F", Accidental.Sharp): 6,
        ("G", Accidental.Flat): 6,
        ("G", Accidental.Natural): 7,
        ("G", Accidental.Sharp): 8,
        ("A", Accidental.Flat): 8,
        ("A", Accidental.Natural): 9,
        ("A", Accidental.Sharp): 10,
        ("B", Accidental.Flat): 10,
        ("B", Accidental.Natural): 11,
        ("B", Accidental.Sharp): 12,
    }

    def __new__(
        cls, octave: int, note: str, accidental: Accidental = Accidental.Natural
    ):
        key = (octave, note, accidental)
        if key not in cls._all_notes:
            note_num = _to_num(octave, note, accidental)
            inst = super().__new__(cls)
            cls._all_notes[key] = inst
            if not note_num in cls._by_num:
                cls._by_num[note_num] = set()
            cls._by_num[note_num].add(inst)

        return cls._all_notes[key]

    def __init__(
        self,
        octave: int,
        note: str,
        accidental: Accidental = Accidental.Natural,
    ):
        self.octave = octave
        self.note = note
        self.accidental = accidental
        self.note_num = _to_num(self.octave, self.note, self.accidental)

    def minor3(self) -> "_Note":

        return self.note_num + 4

    def __repr__(self) -> str:
        return f"{self.note}{self.accidental.to_str()}{self.octave}"


def _to_num(octave: int, note: str, accidental: Accidental) -> int:
    return (octave * 12) + _Note._rel[note, accidental]


def note_above(note: str, amount: int) -> str:
    """Find the note names above, e.g. c + 3 = e"""
    return chr(ord("A") + ((ord(note) - ord("A")) + (amount - 1)) % 7)
