from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    """
    主視窗類別，包含頂部三視圖切換介面
    """

    def __init__(self):
        """
        初始化 MainWindow 类
        """
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        初始化 UI 元素
        """
        self.setWindowTitle("OmniAgent Studio")
        self.setGeometry(100, 100, 800, 600)

        # 創建 QTabWidget 作為頂部三視圖切換介面
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # 添加畫布視圖
        self.canvas_tab = QWidget()
        self.tab_widget.addTab(self.canvas_tab, "畫布")
        self.initCanvasTab()

        # 添加影片編輯視圖
        self.editor_tab = QWidget()
        self.tab_widget.addTab(self.editor_tab, "影片編輯")
        self.initEditorTab()

        # 添加成片視圖
        self.output_tab = QWidget()
        self.tab_widget.addTab(self.output_tab, "成片")
        self.initOutputTab()

    def initCanvasTab(self):
        """
        初始化畫布視圖
        """
        layout = QVBoxLayout()
        label = QLabel("畫布視圖", self.canvas_tab)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.canvas_tab.setLayout(layout)

    def initEditorTab(self):
        """
        初始化影片編輯視圖
        """
        layout = QVBoxLayout()
        label = QLabel("影片編輯視圖", self.editor_tab)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.editor_tab.setLayout(layout)

    def initOutputTab(self):
        """
        初始化成片視圖
        """
        layout = QVBoxLayout()
        label = QLabel("成片視圖", self.output_tab)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.output_tab.setLayout(layout)
