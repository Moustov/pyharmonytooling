from pyharmonytools.guitar.guitar_tab.guitar_tab import GuitarTab


class ConsoleForGuitarTab:
    def __init__(self):
        pass

    @staticmethod
    def display(gt: GuitarTab):
        MARGIN = -1  # todo code smell: magic number defined empirically
        for b in range(0, gt.get_number_of_bars()):
            localized_chords = gt.get_simplest_progressive_chords_in_a_bar(b)
            print("----------------")
            print(f"Bar #{b}:")
            # print(localized_chords)
            chords_line = [" " * gt.get_nb_chars_in_bar(b), " " * gt.get_nb_chars_in_bar(b)]
            chord_number = 0
            previous_end_of_chord_position = 0
            for k in localized_chords.keys():
                current_caret_found = int(k)
                chord = str(localized_chords[k])
                if (current_caret_found - previous_end_of_chord_position) < MARGIN and chord_number != 0:
                    line = 1
                else:
                    line = 0
                before_new_chord = chords_line[line][:current_caret_found + 2] + chord
                chords_line[line] = before_new_chord + chords_line[line][len(before_new_chord):]
                previous_end_of_chord_position = len(before_new_chord)
                chord_number += 1
            if (chords_line[1].strip()):
                print(chords_line[1])
            print(chords_line[0])
            print(gt.bars_ascii[b])
