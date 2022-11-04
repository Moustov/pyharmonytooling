LOD_NONE = 0
LOD_TONE = 1
LOD_CHORD = 2
LOD_NOTE = 3
LOD_ALL = 4
outcome_level_of_detail = LOD_ALL


def print_detail(expected_level_of_detail, message: str):
    if expected_level_of_detail <= outcome_level_of_detail:
        print(message)
