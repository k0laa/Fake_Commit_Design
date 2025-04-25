import datetime

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QColor, QBrush, QPen
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGraphicsView, QGraphicsScene, QComboBox

from ui.theme import DEFAULT_THEME


class CommitPainter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Commit Painter")
        self.setGeometry(100, 100, 1150, 490)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.grid = [[0 for _ in range(53)] for _ in range(7)]
        self.current_level = 1
        self.cell_size = 12
        self.spacing = 3

        self.setStyleSheet(DEFAULT_THEME)
        self.level_colors = ["#0d4429", "#016c31", "#26a641", "#39d353"]

        self.init_ui()

        QTimer.singleShot(100, lambda: self.preview_view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio))


    def init_ui(self):
        layout = QVBoxLayout()

        button_layout = QHBoxLayout()
        self.clear_button = QPushButton("Tümünü Temizle")
        self.clear_button.setObjectName("ClearButton")
        self.clear_button.clicked.connect(self.clear_grid)
        button_layout.addWidget(self.clear_button)

        self.eraser_button = QPushButton("Silgi")
        self.eraser_button.setObjectName("EraseButton")
        self.eraser_button.setCheckable(True)
        self.eraser_button.clicked.connect(lambda: self.set_level(0))
        button_layout.addWidget(self.eraser_button)

        self.level_buttons = []
        for i in range(1, 5):
            btn = QPushButton()
            btn.setCheckable(True)
            btn.setStyleSheet(f"""
                        QPushButton {{
                            background-color: {self.level_colors[i - 1]};
                            border-radius: 20px;
                            border: 3px solid transparent;
                        }}
                        QPushButton:checked {{
                            border: 3px solid yellow;
                        }}
                    """)

            btn.clicked.connect(lambda _, lvl=i: self.set_level(lvl))
            self.level_buttons.append(btn)
            button_layout.addWidget(btn)

        self.year_combo = QComboBox()
        self.years = [str(y) for y in reversed(range(2010, datetime.date.today().year + 1))]
        self.year_combo.addItems(self.years)
        self.year_combo.currentIndexChanged.connect(self.update_scene)
        button_layout.addWidget(self.year_combo)

        layout.addLayout(button_layout)

        self.preview_view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.preview_view.setScene(self.scene)
        self.preview_view.viewport().installEventFilter(self)
        layout.addWidget(self.preview_view)

        self.central_widget.setLayout(layout)
        self.update_scene()


    def set_level(self, level):
        self.current_level = level
        self.eraser_button.setChecked(level == 0)
        for i, btn in enumerate(self.level_buttons):
            btn.setChecked(i + 1 == level)

    def clear_grid(self):
        self.grid = [[0 for _ in range(53)] for _ in range(7)]
        self.update_scene()

    def get_start_date(self, year):
        d = datetime.date(year, 1, 1)
        while d.weekday() != 6:
            d -= datetime.timedelta(days=1)
        return d

    def get_end_date(self, year):
        d = datetime.date(year, 12, 31)
        while d.weekday() != 5:
            d += datetime.timedelta(days=1)
        return d

    def update_scene(self):
        self.scene.clear()

        year = int(self.year_combo.currentText())
        start_date = self.get_start_date(year)
        end_date = self.get_end_date(year)
        weeks_in_year = ((end_date - start_date).days + 1) // 7

        for y in range(7):
            for x in range(weeks_in_year):
                rect_x = x * (self.cell_size + self.spacing)
                rect_y = y * (self.cell_size + self.spacing)
                level = self.grid[y][x] if x < len(self.grid[y]) else 0
                target_date = start_date + datetime.timedelta(weeks=x, days=y)
                if target_date.year != year:
                    color = QColor("#1c1b2f")
                elif level in range(1, 5):
                    color = QColor(self.level_colors[level - 1])
                else:
                    color = QColor("#2d2c45")
                brush = QBrush(color)
                pen = QPen(QColor("#1c1b2f"))
                self.scene.addRect(rect_x, rect_y, self.cell_size, self.cell_size, pen, brush)

        self.preview_view.setSceneRect(self.scene.itemsBoundingRect())
        self.preview_view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

    def eventFilter(self, source, event):
        if source is self.preview_view.viewport():
            if event.type() in [event.MouseButtonPress, event.MouseMove] and event.buttons() == Qt.LeftButton:
                pos = self.preview_view.mapToScene(event.pos())
                cell_space = self.cell_size + self.spacing
                x = int(pos.x() // cell_space)
                y = int(pos.y() // cell_space)
                if 0 <= x < 53 and 0 <= y < 7:
                    target_date = datetime.timedelta(weeks=x, days=y)
                    if target_date:
                        self.grid[y][x] = self.current_level
                        self.update_scene()
                return True
        return super().eventFilter(source, event)
