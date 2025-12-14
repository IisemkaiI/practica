import re
from typing import List


def infix_to_postfix(expr: str) -> List[str]:
    """
    Преобразует инфиксное выражение в ОПН (Reverse Polish Notation).
    Поддерживает: +, -, *, /, (), унарный минус.
    """

    expr = expr.replace(' ', '')
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i] == '-':
            if i == 0 or expr[i - 1] in '(+-*/':
                tokens.append('~')
            else:
                tokens.append('-')
        elif expr[i] in '+*/()':
            tokens.append(expr[i])
        elif expr[i].isdigit() or expr[i] == '.':
            num = ''
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                num += expr[i]
                i += 1
            tokens.append(num)
            continue
        i += 1

    output = []
    stack = []
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '~': 3}
    for token in tokens:
        if re.fullmatch(r'\d+\.?\d*', token):
            output.append(token)
        elif token == '~':
            stack.append(token)
        elif token in '+-*/':
            while (stack and stack[-1] != '(' and
                   stack[-1] in prec and
                   prec[stack[-1]] >= prec[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Несбалансированные скобки")
            stack.pop()
        else:
            raise ValueError(f"Неизвестный токен: {token}")

    while stack:
        if stack[-1] in '()':
            raise ValueError("Несбалансированные скобки")
        output.append(stack.pop())

    return output

def evaluate_postfix(postfix: List[str]) -> float:
    """
    Вычисляет значение выражения в ОПН.
    """
    stack = []
    for token in postfix:
        if token == '~':
            if not stack:
                raise ValueError("Не хватает операнда для унарного минуса")
            a = stack.pop()
            stack.append(-a)
        elif token in '+-*/':
            if len(stack) < 2:
                raise ValueError(f"Не хватает операндов для оператора '{token}'")
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Деление на ноль")
                stack.append(a / b)
        else:

            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError(f"Некорректное число: {token}")

    if len(stack) != 1:
        raise ValueError("Некорректное выражение: лишние операнды")
    return stack[0]


def calculate(expr: str) -> float:
    """
    Принимает инфиксное выражение, возвращает результат.
    """
    try:
        postfix = infix_to_postfix(expr)
        print(f"ОПН: {' '.join(postfix)}")
        result = evaluate_postfix(postfix)
        return result
    except Exception as e:
        raise RuntimeError(f"Ошибка в выражении '{expr}': {e}")



if __name__ == "__main__":
    test_cases = [
        "3 + 4 * 2",
        "(3 + 4) * 2",
        "10 - 2 * 3",
        "2 * (3 + 4) - 5",
        "-5 + 3",
        "(-2) * 3",
        "10 / 2 + 3",
        "2 * -3 + 1",
        "(1 + 2.5) * (3 - 1)",
        "3 + 4 * (2 - 1)",
        "((1+2)*3)^2",
    ]

    print("🧮 Тест калькулятора:")
    for expr in test_cases:
        if '^' in expr:
            print(f"ошибка  '{expr}' — пропущено (возведение в степень не входит в задание)")
            continue
        try:
            res = calculate(expr)
            print(f"истина '{expr}' = {res}")
        except Exception as e:
            print(f"ложь '{expr}' → Ошибка: {e}")


    print("\n" + "="*50)
    print("⌨️  Введите своё выражение (или 'q' для выхода):")
    while True:
        try:
            user_input = input(">>> ").strip()
            if user_input.lower() == 'q':
                break
            if not user_input:
                continue
            result = calculate(user_input)
            print(f"= {result}")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print("!", e)