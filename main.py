import sys
from PyQt5.QtWidgets import QApplication
from windows.commit_painter_window import CommitPainter

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CommitPainter()
    window.show()
    sys.exit(app.exec_())