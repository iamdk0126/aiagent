from PySide6.QtWidgets import QDialog, QVBoxLayout, QTableView, QPushButton, QHBoxLayout, QLabel
from PySide6.QtCore import Qt
from database.db_manager import DBManager
from database.model_store import ModelStore

class ModelStoreDialog(QDialog):
    """
    ModelStoreDialog 類別用於顯示和管理 model_store 資料表中的模型信息。
    """

    def __init__(self, parent=None):
        """
        初始化 ModelStoreDialog 类
        :param parent: 父窗口
        """
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        """
        初始化 UI 元素
        """
        layout = QVBoxLayout()

        # 模型列表顯示
        self.model_table_view = QTableView(self)
        self.model_table_view.setSelectionBehavior(QTableView.SelectRows)
        self.model_table_view.setSelectionMode(QTableView.SingleSelection)
        layout.addWidget(self.model_table_view)

        # 按鈕布局
        button_layout = QHBoxLayout()
        self.refresh_button = QPushButton("刷新", self)
        self.refresh_button.clicked.connect(self.refresh_model_list)
        button_layout.addWidget(self.refresh_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        # 初始化數據庫連接
        self.db_manager = DBManager("sqlite:///path/to/your/database.db")
        self.model_store = ModelStore(self.db_manager)

        # 刷新模型列表
        self.refresh_model_list()

    def refresh_model_list(self):
        """
        刷新模型列表
        """
        models = self.model_store.get_all_models()
        self.model_table_view.setModel(models)
        self.model_table_view.resizeColumnsToContents()
