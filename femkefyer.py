import sys


def main() -> str:
    args = sys.argv
    raw_input = " ".join(args[1:])
    if raw_input == "":
        raw_input = "No input was received"
    print(f"{raw_input=}")
    result = femkefy(raw_input)
    return result


def femkefy(raw_input: str) -> str:
    search_and_replace_couples = {("v", "f"), ("V", "F"), ("z", "s"), ("Z", "S")}
    edit_counter, result = count_and_replace(raw_input, *search_and_replace_couples)
    print(f"{edit_counter=}")
    print(f"{result=}")
    return result


def count_and_replace(raw_input: str, *search_and_replace_couples: (str, str)) -> (int, str):
    """note that order of the couples might matter as the earlier ones change the string the later ones operate on"""
    edit_counter = 0
    for search, replace in search_and_replace_couples:
        edit_counter += raw_input.count(search)
        raw_input = raw_input.replace(search, replace)
    return edit_counter, raw_input


if __name__ == "__main__":
    exit(main())
