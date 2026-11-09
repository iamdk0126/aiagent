from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QComboBox, QLineEdit, QPushButton
from PySide6.QtCore import Qt

class ShotPairNodeWidget(QWidget):
    """
    左圖右影成對分鏡卡、白名單縮圖列、運鏡/布光/參數懸浮框
    """

    def __init__(self, parent=None):
        """
        初始化 ShotPairNodeWidget 类
        :param parent: 父窗口
        """
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        """
        初始化 UI 元素
        """
        layout = QVBoxLayout()

        # 左圖右影成對分鏡卡
        self.left_frame_label = QLabel("左圖", self)
        self.right_frame_label = QLabel("右影", self)
        self.left_frame_layout = QHBoxLayout()
        self.left_frame_layout.addWidget(self.left_frame_label)
        self.right_frame_layout = QHBoxLayout()
        self.right_frame_layout.addWidget(self.right_frame_label)
        layout.addLayout(self.left_frame_layout)
        layout.addLayout(self.right_frame_layout)

        # 白名單縮圖列
        self.white_list_label = QLabel("白名單", self)
        self.white_list_list_widget = QListWidget(self)
        layout.addWidget(self.white_list_label)
        layout.addWidget(self.white_list_list_widget)

        # 運鏡/布光/參數懸浮框
        self.camera_combo_box = QComboBox(self)
        self.lighting_combo_box = QComboBox(self)
        self.parameters_line_edit = QLineEdit(self)
        self.controls_layout = QHBoxLayout()
        self.controls_layout.addWidget(self.camera_combo_box)
        self.controls_layout.addWidget(self.lighting_combo_box)
        self.controls_layout.addWidget(self.parameters_line_edit)
        layout.addLayout(self.controls_layout)

        self.setLayout(layout)

    def add_frame(self, left_frame, right_frame):
        """
        添加左圖右影成對分鏡卡
        :param left_frame: 左圖
        :param right_frame: 右影
        """
        self.left_frame_label.setText(left_frame)
        self.right_frame_label.setText(right_frame)

    def add_to_white_list(self, item):
        """
        將項目添加到白名單
        :param item: 白名單項目
        """
        self.white_list_list_widget.addItem(item)

    def set_camera(self, camera):
        """
        設置運鏡
        :param camera: 運鏡
        """
        self.camera_combo_box.setCurrentText(camera)

    def set_lighting(self, lighting):
        """
        設置布光
        :param lighting: 布光
        """
        self.lighting_combo_box.setCurrentText(lighting)

    def set_parameters(self, parameters):
        """
        設置參數
        :param parameters: 參數
        """
        self.parameters_line_edit.setText(parameters)
