import chess
import chess.svg

from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 560, 560)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 540, 540)

        self.chessBoard = chess.Board()
        self.squares = self.chessBoard.attacks(chess.C2)

        self.chessBoardSvg = chess.svg.board(self.chessBoard, squares=self.squares).encode("UTF-8")
        self.widgetSvg.load(self.chessBoardSvg)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()