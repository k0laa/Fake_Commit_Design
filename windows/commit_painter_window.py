from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

from ui.theme import DEFAULT_THEME


class CommitPainter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Commit Painter")
        self.setGeometry(100, 100, 1150, 490)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.setStyleSheet(DEFAULT_THEME)
        self.level_colors = ["#0d4429", "#016c31", "#26a641", "#39d353"]


        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        button_layout = QHBoxLayout()
        self.clear_button = QPushButton("Tümünü Temizle")
        self.clear_button.setObjectName("ClearButton")
        button_layout.addWidget(self.clear_button)

        self.eraser_button = QPushButton("Silgi")
        self.eraser_button.setObjectName("EraseButton")
        self.eraser_button.setCheckable(True)
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

        layout.addLayout(button_layout)

        self.central_widget.setLayout(layout)

    def set_level(self, level):
        self.current_level = level
        self.eraser_button.setChecked(level == 0)
        for i, btn in enumerate(self.level_buttons):
            btn.setChecked(i + 1 == level)
