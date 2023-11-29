from PyQt6.QtWidgets import *

from solver.solve import solve
from ui.settings import Settings
from solver.stab import calc_stab_time


class LabWinodw(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lab 02")
        self.setFixedSize(Settings.window_width, Settings.window_height)

        self.main_layout = QVBoxLayout()

        self.__create_matrix()
        self.__create_res_table()
        self.main_layout.addStretch()

        widget = QWidget()
        widget.setLayout(self.main_layout)

        self.setCentralWidget(widget)

    def __create_matrix(self):

        self.__create_matrix_meta()

        label = QLabel()
        label.setText("Матрица интенсивностей переходов:")

        self.state_num = self.spin_box.value()
        self.matrix = QTableWidget()
        self.matrix.setRowCount(self.state_num)
        self.matrix.setColumnCount(self.state_num)
        self.matrix.setFixedSize(Settings.matrix_width, Settings.matrix_height)

        layout = QVBoxLayout()
        layout.addLayout(self.__create_matrix_meta())
        layout.addWidget(label)
        layout.addWidget(self.matrix)
        layout.addStretch()

        self.main_layout.addLayout(layout)

    def __create_matrix_meta(self):
        label = QLabel()
        label.setText("Выберите количество состояний:")

        self.spin_box = QSpinBox()
        self.spin_box.setMinimum(2)
        self.spin_box.setMaximum(10)
        self.spin_box.valueChanged.connect(self.__change_table)

        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.spin_box)
        layout.addStretch()

        return layout

    def __create_res_table(self):
        resolve_button = QPushButton("Решить")
        resolve_button.setFixedWidth(Settings.res_button_width)
        resolve_button.clicked.connect(self.__solve)

        label = QLabel("Cреднее относительное время пребывания системы в придельном стационарном состоянии:")

        self.result_table = QTableWidget()
        self.result_table.setRowCount(1)
        self.result_table.setColumnCount(self.state_num)
        self.result_table.setVerticalHeaderItem(0, QTableWidgetItem('P  '))
        self.result_table.setFixedSize(Settings.res_width, Settings.res_height)

        self.time_table = QTableWidget()
        self.time_table.setRowCount(1)
        self.time_table.setColumnCount(self.state_num)
        self.time_table.setVerticalHeaderItem(0, QTableWidgetItem('T  '))
        self.time_table.setFixedSize(Settings.res_width, Settings.res_height)

        layout = QVBoxLayout()
        layout.addWidget(resolve_button)
        layout.addWidget(label)
        layout.addWidget(self.result_table)
        layout.addWidget(self.time_table)
        layout.addStretch()

        self.main_layout.addLayout(layout)

    def __change_table(self):
        cur_state_num = self.spin_box.value()

        if cur_state_num != self.state_num:
            if cur_state_num > self.state_num:
                for i in range(cur_state_num - self.state_num):
                    self.matrix.insertRow(self.state_num + i)
                    self.matrix.insertColumn(self.state_num + i)
                    self.result_table.insertColumn(self.state_num + i)
                    self.time_table.insertColumn(self.state_num + i)
            elif cur_state_num < self.state_num:
                for i in range(self.state_num - cur_state_num):
                    self.matrix.removeRow(self.state_num - i - 1)
                    self.matrix.removeColumn(self.state_num - i - 1)
                    self.result_table.removeColumn(self.state_num - i - 1)
                    self.time_table.removeColumn(self.state_num - i - 1)
            self.state_num = cur_state_num

    def __solve(self):
        try:
            if self.state_num < 2:
                raise Exception('Должно быть задано не менее 2 состояний')
            data = self.__get_mtr()
            res = solve(data)
            st, tl, prob = calc_stab_time(data, res)
            self.__show_result(res, st)
        except Exception as e:
            self.__error_msg(str(e))

    def __get_mtr(self):
        matrix = []

        for i in range(self.state_num):
            matrix.append([])
            for j in range(self.state_num):
                try:
                    item = self.matrix.model().index(i, j).data()
                    if i == j:
                        item = 0
                    elif item is None:
                        item = 0
                    else:
                        item = self.__check_item(item)
                except Exception as e:
                    raise e
                else:
                    matrix[i].append(item)

        return matrix

    def __check_item(self, item):
        try:
            item = float(item)
        except:
            raise ValueError('Интенсивность перехода должна быть вещественным числом.')
        else:
            if item < 0:
                raise ValueError('Интенсивность перехода должна быть неотрицательной.')

        return item

    def __error_msg(self, text):
        msg = QMessageBox()

        msg.setText(text)
        msg.setWindowTitle("Ошибка")

        msg.exec()

    def __show_result(self, res, tm):
        eps = 1e-4
        for i, res in enumerate(res):
            self.result_table.setItem(0, i, QTableWidgetItem(str(0 if res < eps else round(res, 4))))
        for i, res in enumerate(tm):
            self.time_table.setItem(0, i, QTableWidgetItem(str(0 if res < eps else round(res, 4))))
