PAGES_NUM = 7  # число "страниц" в файле
ROWS_PER_PAGE = 50  # число "строк на странице"
COLS_PER_ROW = 50  # число "цифр на строке"

SYMBOLS_PER_PAGE = ROWS_PER_PAGE * COLS_PER_ROW  # число "цифр на странице"
SYMBOLS_NUM = SYMBOLS_PER_PAGE * PAGES_NUM # общее число цифр в файле

class TabularGenerator:

    def __init__(self):

        # начальная позиция в файле
        page = 0
        row = 0
        column = 14

        self.position = SYMBOLS_PER_PAGE * page + COLS_PER_ROW * row + column

    def gen_number(self, digits=1):
        num = -1
        with open("data/random_numbers.txt", "r") as f:
            flag = True

            while flag:
                f.seek(self.position, 0)

                num = int(f.read(digits))

                # проверка не первые ли нули
                if num // (10 ** (digits - 1)) >= 1:
                   flag = False

                # сдвигаем позицию
                self.position += COLS_PER_ROW

                # дошли до конца файла - возвращаемся в начало
                if self.position > SYMBOLS_NUM - 1:
                    self.position %= SYMBOLS_NUM
                    self.position += 1

        return num

    def gen_sequence(self, digits, length):
        sequence = []

        for _ in range(length):
            sequence.append(self.gen_number(digits))

        return sequence