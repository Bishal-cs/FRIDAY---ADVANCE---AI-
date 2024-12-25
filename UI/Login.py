import sys
from UI.Friday import ui
from PyQt5 import QtWidgets, QtGui, QtCore

class FridayLoginPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.start_animations()
        self.login_form_visible = False

    def setup_ui(self):
        self.setWindowTitle("Friday Login")
        self.setGeometry(100, 100, 400, 600)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.main_container = QtWidgets.QWidget(self)
        self.main_container.setGeometry(50, 50, 300, 500)
        self.main_container.setStyleSheet("""
            background-color: rgba(0, 0, 0, 150);
            border-radius: 20px;
            border: 2px solid #00ffff;
        """)
        self.main_container.setVisible(False)

        self.title_label = QtWidgets.QLabel("Welcome to Friday", self.main_container)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setGeometry(20, 30, 260, 50)
        self.title_label.setStyleSheet("""
            color : #00ffff;
            font-size : 18px;
            font-weight : bold;
            font-family : 'Orbitron';
        """)

        self.username_input = self.create_input_field("Username", 100)
        self.password_input = self.create_input_field("Password", 150, password=True)

        self.login_button = QtWidgets.QPushButton("Login", self.main_container)
        self.login_button.setGeometry(50, 230, 200, 40)
        self.login_button.setStyleSheet("""
            background-color : rgba(0, 0, 0, 180);
            color : #00ffff;
            font-size : 16px;
            font-weight : bold;
            border : 2px solid #00ffff;
            border-radius : 20px;
        """)
        self.login_button.clicked.connect(self.on_login)

        glow_effect = QtWidgets.QGraphicsDropShadowEffect(self.login_button)
        glow_effect.setBlurRadius(25)
        glow_effect.setColor(QtGui.QColor(0, 255, 255))
        self.login_button.setGraphicsEffect(glow_effect)

        self.toggle_button = QtWidgets.QPushButton(self)
        self.toggle_button.setIcon(QtGui.QIcon(QtGui.QPixmap("Static/logo.gif")))
        self.toggle_button.setIconSize(QtCore.QSize(60, 60))
        self.toggle_button.setGeometry(310, 10, 60, 60)
        self.toggle_button.setStyleSheet("border: none;")
        self.toggle_button.clicked.connect(self.toggle_login_form)
        self.toggle_button.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)

        self.oldPos = self.pos()

    def create_input_field(self, placeholder, y, password=False):
        input_field = QtWidgets.QLineEdit(self.main_container)
        input_field.setGeometry(50, y, 200, 40)
        input_field.setPlaceholderText(placeholder)
        input_field.setStyleSheet("""
            background-color : rgba(255, 255, 255, 50);
            color : #00ffff;
            font-size : 14px;
            border : 2px solid #00ffff;
            border-radius : 10px;
        """)
        if password:
            input_field.setEchoMode(QtWidgets.QLineEdit.Password)

        glow_effect = QtWidgets.QGraphicsDropShadowEffect(input_field)
        glow_effect.setBlurRadius(15)
        glow_effect.setColor(QtGui.QColor(0, 255, 255))
        input_field.setGraphicsEffect(glow_effect)

        return input_field
        
    def start_animations(self):
        self.title_animation = QtCore.QPropertyAnimation(self.title_label, b"windowOpacity")
        self.title_animation.setDuration(1500)
        self.title_animation.setStartValue(0)
        self.title_animation.setEndValue(1)

        self.login_button_glow_animation = QtCore.QPropertyAnimation(self.login_button.graphicsEffect(), b"blurRadius")
        self.login_button_glow_animation.setDuration(1000)
        self.login_button_glow_animation.setStartValue(20)
        self.login_button_glow_animation.setEndValue(35)
        self.login_button_glow_animation.setLoopCount(-1)
        self.login_button_glow_animation.start()

    def toggle_login_form(self):
        if self.login_form_visible:
            self.main_container_animation = QtCore.QPropertyAnimation(self.main_container, b"geometry")
            self.main_container_animation.setDuration(800)
            self.main_container_animation.setStartValue(self.main_container.geometry())
            self.main_container_animation.setEndValue(QtCore.QRect(50, -500, 300, 500))
            self.main_container_animation.setEasingCurve(QtCore.QEasingCurve.InBack)
            self.main_container_animation.finished.connect(lambda: self.main_container.setVisible(False))
            self.main_container_animation.start()
        else:
            self.main_container.setVisible(True)
            self.main_container_animation = QtCore.QPropertyAnimation(self.main_container, b"geometry")
            self.main_container_animation.setDuration(800)
            self.main_container_animation.setStartValue(QtCore.QRect(50, -500, 300, 500))
            self.main_container_animation.setEndValue(QtCore.QRect(50, 50, 300, 500))
            self.main_container_animation.setEasingCurve(QtCore.QEasingCurve.OutBounce)
            self.main_container_animation.start()

            self.title_animation.start()
        self.login_form_visible = not self.login_form_visible

    def on_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "Bishal" and password == "Friday":
            ui()
        else:
            print("Invalid Credentials")

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

def login():
    app = QtWidgets.QApplication(sys.argv)
    window = FridayLoginPage()
    window.show()
    sys.exit(app.exec_())
