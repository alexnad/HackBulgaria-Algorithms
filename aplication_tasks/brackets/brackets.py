OPEN_CURLY = '{'
CLOSE_CURLY = '}'
OPEN_ANGULAR = '['
CLOSE_ANGULAR = ']'
OPEN_ROUND = '('
CLOSE_ROUND = ')'
INVALID_EXPRESSION_ERROR = 'NO'
DIGITS = '0123456789'


def get_expression():
    return input('Enter expression>')


class InvalidExpressionError(Exception):
    pass


def main():
    expression = get_expression()
    try:
        if expression[0] == OPEN_CURLY:
            result = evaluate_curly(iter(expression[1:]))
        elif expression[0] == OPEN_ANGULAR:
            result = evaluate_angular(iter(expression[1:]))
        elif expression[0] == OPEN_ROUND:
            result = evaluate_round(iter(expression[1:]))
        else:
            raise INVALID_EXPRESSION_ERROR
    except InvalidExpressionError:
        result = INVALID_EXPRESSION_ERROR

    print(result)


def evaluate_curly(expression):
    value = 0
    digits = []
    for symbol in expression:
        if symbol in DIGITS:
            digits.insert(0, symbol)
        elif symbol == OPEN_ANGULAR:
            value += sum_digits(digits) + 2 * evaluate_angular(expression)
        elif symbol == CLOSE_CURLY:
            try:
                expression.__next__()
            except StopIteration:
                value += sum_digits(digits)
                return value
        else:
            raise InvalidExpressionError


def evaluate_angular(expression):
    digits = []
    value = 0
    for symbol in expression:
        if symbol in DIGITS:
            digits.insert(0, symbol)
        elif symbol == OPEN_ROUND:
            value += sum_digits(digits) + 2 * evaluate_round(expression)
        elif symbol == CLOSE_ANGULAR:
            value += sum_digits(digits)
            return value
        else:
            break
    raise InvalidExpressionError


def evaluate_round(expression):
    digits = []
    value = 0
    for symbol in expression:
        if symbol in DIGITS:
            digits.insert(0, symbol)
        elif symbol == CLOSE_ROUND:
            value += sum_digits(digits)
            return value
        else:
            break
    raise InvalidExpressionError


def sum_digits(digits):
    result = sum([int(digit) * (10 ** power) for power, digit in enumerate(digits)])
    digits[:] = []
    return result
