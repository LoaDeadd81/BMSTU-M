import sys

from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow

from algorithmic_generator import MersonVortex
from tabular_generator import TabularGenerator
from criterion import RandomnessCriterion


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnGenAlg.clicked.connect(self.gen_alg)

        self.ui.btnGenTable.clicked.connect(self.gen_tabular)

        self.inputNum = 10
        self.init_input_table()
        self.ui.btnCaclInput.clicked.connect(self.calc_user_input)


    def gen_alg(self):
        number = self.ui.sbAlg.value()
        #number = 10

        sequences = [
            MersonVortex(1).gen_sequence(0, 10, number),
            MersonVortex(1).gen_sequence(10, 100, number),
            MersonVortex(1).gen_sequence(100, 1000, number)
        ]

        self.ui.twAlg.setRowCount(number)
        self.ui.twAlg.setColumnCount(3)
        self.ui.twAlg.setHorizontalHeaderLabels(["1 разряд", "2 разряда", "3 разряда"])
        self.ui.twAlg.horizontalHeader().setSectionResizeMode(
                QtWidgets.QHeaderView.Stretch)

        coefficients = []

        for j, sequence in enumerate(sequences):
            for i in range(number):
                item = QtWidgets.QTableWidgetItem(str(sequence[i]))
                self.ui.twAlg.setItem(i, j, item)

            coefficients.append(RandomnessCriterion().get_coeff_my(sequence))

        self.ui.twCoefAlg.setRowCount(1)
        self.ui.twCoefAlg.setVerticalHeaderLabels(["K"])
        self.ui.twCoefAlg.setColumnCount(3)
        self.ui.twCoefAlg.setHorizontalHeaderLabels(["1 разряд", "2 разряда", "3 разряда"])
        self.ui.twCoefAlg.horizontalHeader().setSectionResizeMode(
                QtWidgets.QHeaderView.Stretch)

        for j, coefficient in enumerate(coefficients):
            item = QtWidgets.QTableWidgetItem("{0:0.3f}".format(coefficient))
            self.ui.twCoefAlg.setItem(0, j, item)


    def gen_tabular(self):
        number = self.ui.sbTable.value()
        #number = 10

        sequences = [
            TabularGenerator().gen_sequence(1, number),
            TabularGenerator().gen_sequence(2, number),
            TabularGenerator().gen_sequence(3, number)
        ]

        self.ui.twTable.setRowCount(number)
        self.ui.twTable.setColumnCount(3)
        self.ui.twTable.setHorizontalHeaderLabels(["1 разряд", "2 разряда", "3 разряда"])
        self.ui.twTable.horizontalHeader().setSectionResizeMode(
                QtWidgets.QHeaderView.Stretch)

        coefficients = []

        for j, sequence in enumerate(sequences):
            for i in range(number):
                item = QtWidgets.QTableWidgetItem(str(sequence[i]))
                self.ui.twTable.setItem(i, j, item)

            coefficients.append(RandomnessCriterion().get_coeff_my(sequence))

        self.ui.twCoefTable.setRowCount(1)
        self.ui.twCoefTable.setVerticalHeaderLabels(["K"])
        self.ui.twCoefTable.setColumnCount(3)
        self.ui.twCoefTable.setHorizontalHeaderLabels(["1 разряд", "2 разряда", "3 разряда"])
        self.ui.twCoefTable.horizontalHeader().setSectionResizeMode(
                QtWidgets.QHeaderView.Stretch)

        for j, coefficient in enumerate(coefficients):
            item = QtWidgets.QTableWidgetItem("{0:0.3f}".format(coefficient))
            self.ui.twCoefTable.setItem(0, j, item)


    def init_input_table(self):

        self.ui.twInput.setRowCount(self.inputNum)
        self.ui.twInput.setColumnCount(1)
        self.ui.twInput.setHorizontalHeaderLabels(["Числа"])
        self.ui.twInput.horizontalHeader().setSectionResizeMode(
                QtWidgets.QHeaderView.Stretch)

        for i in range(self.inputNum):
            sbCell = QtWidgets.QSpinBox()
            sbCell.setMinimum(-1000)
            sbCell.setMaximum(1000)
            sbCell.setSingleStep(1)

            self.ui.twInput.setCellWidget(i, 0, sbCell)

    def calc_user_input(self):
        sequence = [self.ui.twInput.cellWidget(i, 0).value()
                        for i in range(self.inputNum)]

        coeff = RandomnessCriterion().get_coeff_my(sequence)

        self.ui.dsbCoefInput.setValue(coeff)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()