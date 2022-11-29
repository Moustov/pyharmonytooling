class NoteFretCaret:
    def __init__(self, current_notes: [], fret: int, current_caret: int, fingers_involved_qty: int, string_name: str):
        self.current_notes = current_notes
        self.fret = fret
        self.current_caret = current_caret
        self.string_name = string_name
        self.fingers_involved_qty = fingers_involved_qty
