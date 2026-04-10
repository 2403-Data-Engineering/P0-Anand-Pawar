import re


def is_blank(value):
    return value is None or str(value).strip() == ""


def is_valid_email(email):
    if is_blank(email):
        return False
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.fullmatch(pattern, email.strip()) is not None


def is_valid_name(name):
    if is_blank(name):
        return False

    name = name.strip()

    if name.isdigit():
        return False

    pattern = r"^[A-Za-z][A-Za-z\s'\-]*$"
    return re.fullmatch(pattern, name) is not None


def is_valid_text_field(value):
    if is_blank(value):
        return False

    value = value.strip()

    if value.isdigit():
        return False

    return True


def is_valid_subject_code(code):
    if is_blank(code):
        return False

    code = code.strip()

    pattern = r"^[A-Za-z]{2,10}[0-9]{0,5}$"
    return re.fullmatch(pattern, code) is not None