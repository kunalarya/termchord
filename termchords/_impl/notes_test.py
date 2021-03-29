import _impl.notes as notes


def test_all_notes():
    assert len(notes.notes()) == 12
