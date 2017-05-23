def compress(string):
    if string is None or not string:
        return string
    result = ''
    prev_char = string[0]
    count = 0
    for char in string:
        if char == prev_char:
            count += 1
        else:
            result += calc_partial_result(prev_char, count)
            prev_char = char
            count = 1
    result += calc_partial_result(prev_char, count)
    return result if len(result) < len(string) else string


def calc_partial_result(prev_char, count):
    return prev_char + (str(count) if count > 1 else '')