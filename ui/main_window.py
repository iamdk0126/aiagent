from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QFrame, QHBoxLayout, QLabel as QLabelText
from PySide6.QtCore import Qt, QTimer
import psutil

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

        # 添加硬體遙測狀態視圖
        self.hardware_monitor_tab = QWidget()
        self.tab_widget.addTab(self.hardware_monitor_tab, "硬體遙測狀態")
        self.initHardwareMonitorTab()

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

    def initHardwareMonitorTab(self):
        """
        初始化硬體遙測狀態視圖
        """
        layout = QVBoxLayout()

        # GPU VRAM 與溫度顯示
        self.gpu_monitor_frame = QFrame()
        self.gpu_monitor_frame.setFrameShape(QFrame.Box)
        self.gpu_monitor_frame.setLineWidth(1)
        gpu_layout = QVBoxLayout()

        self.gpu_vram_label = QLabelText("GPU VRAM: 0GB / 0GB", self.gpu_monitor_frame)
        gpu_layout.addWidget(self.gpu_vram_label)

        self.gpu_temp_label = QLabelText("GPU 温度: 0°C", self.gpu_monitor_frame)
        gpu_layout.addWidget(self.gpu_temp_label)

        self.gpu_monitor_frame.setLayout(gpu_layout)
        layout.addWidget(self.gpu_monitor_frame)

        self.hardware_monitor_tab.setLayout(layout)

        # 定期更新硬體遙測狀態
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateHardwareMonitor)
        self.timer.start(1000)  # 每秒更新一次

    def updateHardwareMonitor(self):
        """
        更新硬體遙測狀態
        """
        try:
            # 获取 GPU VRAM 使用情况
            process = psutil.Process()
            vram_usage = process.memory_info().rss / (1024 ** 3)  # 转换为 GB
            vram_total = psutil.virtual_memory().total / (1024 ** 3)  # 转换为 GB

            # 获取 GPU 温度
            temps = psutil.sensors_temperatures()
            gpu_temp = temps['nvidia'][0].current if 'nvidia' in temps else 0

            self.gpu_vram_label.setText(f"GPU VRAM: {vram_usage:.2f}GB / {vram_total:.2f}GB")
            self.gpu_temp_label.setText(f"GPU 温度: {gpu_temp}°C")
        except Exception as e:
            print(f"Error updating hardware monitor: {e}")
