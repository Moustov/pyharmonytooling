from pyharmonytools.guitar_tab.guitar_tab import GuitarTab


class ConsoleForGuitarTab:
    def __init__(self):
        pass

    @staticmethod
    def display(gt: GuitarTab):
        for b in range(0, gt.get_number_of_bars()):
            MARGIN = 1
            localized_chords = gt.get_simplest_progressive_chords_in_a_bar(b)
            print("----------------")
            print("Bar #", b, ":")
            print(localized_chords)
            chords_line = [" " * gt.get_nb_chars_in_bar(b), " " * gt.get_nb_chars_in_bar(b)]
            chord_number = 0
            previous_end_of_chord_position = 0
            for k in localized_chords.keys():
                current_caret_found = int(k)
                chord = str(localized_chords[k])
                before_new_chord = chords_line[chord_number % 2][:current_caret_found + 2] + chord
                line = chord_number % 2
                chords_line[line] = before_new_chord \
                                    + chords_line[line % 2][len(before_new_chord):]
                chord_number += 1
            print(chords_line[1])
            print(chords_line[0])
            print(gt.bars_ascii[b])
