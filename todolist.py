import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget

class Todolist(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application todolist")
        # creation du layout pour window
        self.setGeometry(100,100,500,300)
        self.tasks = []
        self.layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.add_button = QPushButton("Ajoutez une tache !!")
        self.task_list = QListWidget()
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.task_list)
        self.add_button.clicked.connect(self.add_task)
        self.setLayout(self.layout)
    def add_task(self):
        task = self.input_field.text()
        if task:
            self.tasks.append(task)
            self.task_list.addItem(task)
            self.input_field.clear()    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Todolist()
    window.show()
    sys.exit(app.exec_())        
        
#projet1 desktop
      

