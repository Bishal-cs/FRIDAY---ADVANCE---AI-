import sys
import math
import random
from PyQt5.QtCore import Qt, QTimer, pyqtSlot
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QFont
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsTextItem

class FridayUI(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background: transparent;")
        self.initUI()

        # Animation properties
        self.angle = 0
        self.pulse_scale = 1
        self.pulse_direction = 1
        self.scan_angle = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(50) # Adjusted timer interval for smoother performance

    def initUI(self):
        screen_geometry = QApplication.desktop().screenGeometry()
        self.setGeometry(0, 0, screen_geometry.width(), screen_geometry.height())
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setRenderHint(QPainter.Antialiasing)
        
        # Arc Reactor Setup
        self.createArcReactor()
        self.createGlowEffect()
        self.createRadialLines()
        self.createParticles()
        self.createRadarCircles()
        self.createScanLine()
        self.createTextDisplays()

    def createArcReactor(self):
        self.arc_reactor = QGraphicsEllipseItem(-60, -60, 120, 120)
        self.arc_reactor.setBrush(QBrush(QColor(0, 200, 255, 180)))
        self.arc_reactor.setPen(QPen(QColor(255, 255, 255, 200), 2))
        self.scene.addItem(self.arc_reactor)

        for i in range(1, 4):
            ring = QGraphicsEllipseItem(-50 + i * 10, -50 + i * 10, 100 - i * 20, 100 - i * 20)
            ring.setPen(QPen(QColor(255, 255, 255, 150 - i * 30), 2))
            self.scene.addItem(ring)

    def createGlowEffect(self):
        self.glow_item = QGraphicsEllipseItem(-200, -200, 400, 400)
        self.glow_item.setPen(QPen(Qt.NoPen))
        self.glow_item.setBrush(QBrush(QColor(0, 150, 255, 30)))
        self.scene.addItem(self.glow_item)

    def createRadialLines(self):
        self.lines = []
        for angle in range(0, 360, 20):
            line = QGraphicsLineItem(0, 0, 150, 0)
            line.setPen(QPen(QColor(0, 200, 255, 120), 1))
            line.setRotation(angle)
            self.scene.addItem(line)
            self.lines.append(line)

    def createParticles(self):
        self.particles = []
        for _ in range(30):
            x, y = random.randint(-150, 150), random.randint(-150, 150)
            particle = QGraphicsEllipseItem(x, y, 3, 3)
            particle.setBrush(QBrush(QColor(255, 255, 255, 200)))
            self.scene.addItem(particle)
            self.particles.append(particle)

    def createRadarCircles(self):
        self.radar_circles = []
        for i in range(3):
            radar_circle = QGraphicsEllipseItem(-250 - (i * 50), -250 - (i * 50), 500 + (i * 100), 500 + (i * 100))
            radar_circle.setPen(QPen(QColor(0, 255, 255, 100 - i * 30), 1))
            self.scene.addItem(radar_circle)
            self.radar_circles.append(radar_circle)

    def createScanLine(self):
        self.scan_line = QGraphicsLineItem(0, 0, 250, 0)
        self.scan_line.setPen(QPen(QColor(0, 255, 255, 150), 2))
        self.scene.addItem(self.scan_line)

    def createTextDisplays(self):
        self.text_items = []
        texts = [
            "FRIDAY INTERFACE ACTIVE",
            "SCANNING ... ",
            "SYSTEM STATUS: OPTIMAL",
            "SENSORS: ONLINE",
            "DATA LINK: ACTIVE"
        ]
        for i, text in enumerate(texts):
            text_item = QGraphicsTextItem(text)
            text_item.setDefaultTextColor(QColor(0, 200, 255))
            text_item.setFont(QFont("Arial", 12))
            text_item.setPos(-100, 220 + i * 30)
            self.scene.addItem(text_item)
            self.text_items.append(text_item)

    @pyqtSlot()
    def animate(self):
        self.angle = (self.angle + 2) % 360

        # Pulse effect on arc reactor and glow
        self.pulse_scale += 0.01 * self.pulse_direction
        if self.pulse_scale > 1.2 or self.pulse_scale < 0.9:
            self.pulse_direction *= -1
        self.arc_reactor.setScale(self.pulse_scale)
        self.glow_item.setScale(self.pulse_scale * 1.1)

        # Radial lines rotation
        for i, line in enumerate(self.lines):
            line.setRotation(self.angle + i * 15)

        # Particles with reduced movement updates
        for particle in self.particles:
            dx, dy = random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)
            particle.moveBy(dx, dy)

        # Radar circles with pulse effect
        for i, circle in enumerate(self.radar_circles):
            scale = 1 + 0.1 * math.sin(self.angle * 0.1 + i * 0.5)
            circle.setScale(scale)

        # Scanning line rotation
        self.scan_angle = (self.scan_angle + 3) % 360
        self.scan_line.setRotation(self.scan_angle)

        # Update dynamic text
        self.text_items[1].setPlainText(f"SCANNING ... {self.scan_angle}°")
        self.text_items[2].setPlainText(f"SYSTEM STATUS: OPTIMAL ({int(self.pulse_scale * 100)}%)")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

def ui():
    friday_ui = FridayUI()
    friday_ui.showFullScreen()