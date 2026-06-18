from PyQt5.QtWidgets import QApplication, QWidget, QPushButton , QMessageBox

app=QApplication([])


window=QWidget()

window.setGeometry(100, 100, 300, 200)  # x, y, width, height


button=QPushButton("Hello beta", parent = window)
button.move(80,100)

def on_button_clicked():
    QMessageBox.information(window, "Message", "You clicked the button!")

button.clicked.connect(on_button_clicked)

window.show()

app.exec_()



