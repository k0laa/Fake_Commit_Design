DEFAULT_THEME = """
            QWidget {
                background-color: #1c1b2f;
                color: #e0e6f0;
                font-family: 'Segoe UI';
            }
            QPushButton {
                border-radius: 20px;
                padding: 10px;
                min-width: 40px;
                min-height: 40px;
            }
            QPushButton#ClearButton, QPushButton#EraseButton {
                min-width: 100px;
                max-width: 100px;
            }
            QPushButton#ClearButton {
                background-color: #8a7fd3;
                color: white;
            }
            QPushButton#ClearButton:hover {
                background-color: #a299e0;
            }
            QPushButton#EraseButton {
                background-color: #444;
                color: white;
                border: 3px solid transparent;
            }
            QPushButton#EraseButton:checked {
                border: 3px solid yellow;
            }
            QPushButton#EraseButton:hover {
                background-color: #666;
            }
            QComboBox {
                background-color: #3a375c;
                color: #ffffff;
                border: 1px solid #444;
                padding: 5px;
                border-radius: 6px;
                min-width: 80px;
            }
            QComboBox QAbstractItemView {
                background-color: #1c1b2f;
                color: white;
                selection-background-color: #444;
                selection-color: white;
            }
            QPushButton#CommitButton {
                background-color: #9f5fff;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 8px 16px;
                border: 2px solid #6c2cff;
            }
            QPushButton#CommitButton:hover {
                background-color: #b278ff;
            }
        """
