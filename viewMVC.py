from PyQt5 import QtWidgets, QtGui
import sys

class DrawView(QtWidgets.QMainWindow):
    def __init__(self, **kwargs):
        super(DrawView,self).__init__(**kwargs)

        self.setWindowTitle("Losování")
        self.setFixedSize(500,300)
        self.controller=None
        self.model=None
        self.init_gui()
        self.show()

    def init_gui(self):
        DrawView = QtWidgets.QWidget()
        formLayout = QtWidgets.QVBoxLayout()
        DrawView.setLayout(formLayout)
        self.questionLabel = QtWidgets.QLabel("0", self)
        self.questionLabel.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Black))
        self.questionLabel.setWordWrap(True)
        self.questionLabel.setText("")
        formLayout.addWidget(self.questionLabel)
        self.drawButton = QtWidgets.QPushButton("Vylosuj", self)
        self.drawButton.setGeometry(200, 150, 100, 40)
        self.drawButton.clicked.connect(self.clickButton)
        formLayout.addWidget(self.drawButton)
        formLayout.addStretch()
        self.setCentralWidget(DrawView)
    
    def set_controller(self,controller):
        self.controller=controller

    def set_model(self,model):
        self.model=model
    
    def clickButton(self):
        self.controller.draw()
        q=self.model.get_question()
        self.display_question(q)
    
    def display_question(self, question):
        if question==None:
            self.questionLabel.setText("Už není žádná otázka.")
        else:
            self.questionLabel.setText(question[1])


