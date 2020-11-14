CHARS_TO_ESCAPE = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']


def escape_telegram_message_with_markdown(text: str) -> str:
    for char in CHARS_TO_ESCAPE:
        text = text.replace(char, f'\\{char}')
    return text
