import enum
from typing import Dict, Tuple


class Accidental(enum.Enum):
    Natural = enum.auto()
    Sharp = enum.auto()
    Flat = enum.auto()


def notes() -> Dict[int, "_Note"]:
    if not _Note._all_notes:
        # Create all notes.
        note_number = 0
        for i in range(7):
            note_chr = chr(ord("A") + i)
            _ = _Note(note_number, note_chr)

            # Add sharps and flats.
            _ = _Note(note_number, note_chr, Accidental.Sharp)
            _ = _Note(note_number, note_chr, Accidental.Flat)

            note_number += 1
            if note_chr not in ("B", "E"):
                # account for sharps.
                note_number += 1
            if note_chr not in ("C", "F"):
                # account for flats.
                note_number += 1
    return _Note._all_notes


class _Note:
    _all_notes: Dict[Tuple[int, Accidental], "_Note"] = {}

    def __new__(
        cls, note_num: int, note: str, accidental: Accidental = Accidental.Natural
    ):
        if (note, accidental) not in cls._all_notes:
            inst = super().__new__(cls)
            # inst.__init__(note_num, note, accidental)
            cls._all_notes[note, accidental] = inst

        return cls._all_notes[note, accidental]

    def __init__(
        self, note_num: int, note: str, accidental: Accidental = Accidental.Natural
    ):
        self.note = note
        self.accidental = accidental
