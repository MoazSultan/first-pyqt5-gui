from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel

app = QApplication([])

window = QWidget()
window.setWindowTitle("Task 3 - Input and Show")
window.setGeometry(100, 100, 500, 300)  # Larger window

input_box = QLineEdit(window)
input_box.setPlaceholderText("Enter your name")
input_box.move(100, 40)

label = QLabel( window)
label.setFixedWidth(300)  # Wider label
label.move(100, 110)

button = QPushButton("Show Text", parent =window)
button.move(100, 80)

def on_button_click():
    text = input_box.text()
    label.setText("Hello, " + text)

button.clicked.connect(on_button_click)

window.show()
app.exec_()
