from PyQt5.QtWidgets import QMainWindow, QWidget


class CommitPainter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Commit Painter")
        self.setGeometry(100, 100, 500, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.setStyleSheet("""
            QWidget {
                background-color: #1c1b2f;
                color: #e0e6f0;
                font-family: 'Segoe UI';
            }
        """)
