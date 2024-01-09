import sys

from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow

from event_model import EventModel
from step_model import StepModel
from generator import Generator
from memory import Memory
from processor import Processor
from distributions import Uniform, Poisson, Uniform2, Poisson2

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sbMaxLenStep.setDisabled(True)
        self.ui.sbMaxLenEvent.setDisabled(True)
        self.ui.btnRun.clicked.connect(self.run)


    def run(self):
        a, b = self.ui.dsbA.value(), self.ui.dsbB.value()
        lam = self.ui.dsbLambda.value()
        num = self.ui.sbRequestNum.value()
        percent = int(self.ui.dsbProbability.value() * 100)
        delta_t = self.ui.dsbDeltaT.value()

        generator = Generator(Uniform(a, b))
        memory = Memory()
        processor = Processor(Poisson(lam))

        event_model = EventModel(generator, memory, processor, num, percent)
        event_model_result = event_model.run()

        generator = Generator(Uniform(a, b))
        memory = Memory()
        processor = Processor(Poisson(lam))

        step_model = StepModel(generator, memory, processor,
                               num, percent, delta_t)
        step_model_result = step_model.run()

        self.ui.sbMaxLenEvent.setValue(event_model_result)

        self.ui.sbMaxLenStep.setValue(step_model_result)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()