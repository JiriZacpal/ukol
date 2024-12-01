from PyQt5 import QtWidgets
import sys
from model import DrawModel
from viewMVC import DrawView
from controllerMVC import DrawController

app = QtWidgets.QApplication(sys.argv)
model = DrawModel("KMI/XSTR")
view = DrawView()
controller = DrawController(model, view)
view.set_controller(controller)
view.set_model(model)

sys.exit(app.exec_())