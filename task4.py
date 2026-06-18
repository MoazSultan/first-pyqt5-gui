import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

# Create the application and window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Task 4 - Button Click")
window.setGeometry(100, 100, 100, 800)

# Create a label and set its initial text
label = QLabel("Click the button!", window)
label.move(100, 50)

# Create a button
button = QPushButton("Click me!", window)
button.move(50, 50)
button.resize(50,100)

# Define a function to change the label's text
def change_text():
    label.setText("Button clicked!")

# Connect the button's clicked signal to the function
button.clicked.connect(change_text)

# Show the window and run the application
window.show()

app.exec_()