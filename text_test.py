from text import TextUtilities

def test_count_words():
    text_util = TextUtilities("Hello world! This is a test.")
    assert text_util.count_words() == 6

def test_unique_words():
    text_util = TextUtilities("Hello world! Hello everyone.")
    unique_words = text_util.unique_words()
    assert set(unique_words) == {"hello", "world!", "everyone."}

def test_reverse_string():
    text_util = TextUtilities("Hello world!")
    assert text_util.reverse_string() == "!dlrow olleH"

