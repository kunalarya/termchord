import _impl.notes as notes


def test_caching():
    note0 = notes._Note(octave=0, note="E", accidental=notes.Accidental.Sharp)
    note1 = notes._Note(octave=0, note="E", accidental=notes.Accidental.Sharp)
    assert note0 is note1


def test_above():
    assert notes.note_above("A", 3) == "C"
    assert notes.note_above("G", 3) == "B"
    assert notes.note_above("G", 5) == "D"
    assert notes.note_above("F", 8) == "F"


def test_by_num():
    notes.notes()
    assert notes._Note._by_num[5] == {
        notes._Note(octave=0, note="E", accidental=notes.Accidental.Sharp),
        notes._Note(octave=0, note="F", accidental=notes.Accidental.Natural),
    }
