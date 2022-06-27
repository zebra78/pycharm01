def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """
    try:
        return text[0:text.index(" ")]
    except ValueError:
        return text[0:len(text)]


def is_acceptable_password(text: str) -> bool:
    if len(text) > 5:
        return True
    return False


def number_length(a: int) -> int:
    return len(str(a))


if __name__ == "__main__":
    assert number_length(2)
    assert number_length(23)
    assert number_length(34567)

    # assert is_acceptable_password('short')
    # assert is_acceptable_password('muchlonger')

    # print(first_word("Hello world"))
    # print(first_word("single"))
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert first_word("Hello world") == "Hello"
    # assert first_word("a word") == "a"
    # assert first_word("hi") == "hi"
    # print("Coding complete? Click 'Check' to earn cool rewards!")


