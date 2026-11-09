from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt
from typing import Optional

class SettingsBudgetDialog(QDialog):
    """
    設置預算設置對話框
    """
    def __init__(self, parent=None):
        """
        初始化方法
        """
        super().__init__(parent)
        self.setWindowTitle("預算設置")
        self.initUI()

    def initUI(self):
        """
        初始化 UI 元素
        """
        layout = QVBoxLayout()

        self.label = QLabel("預算上限 (USD):", self)
        layout.addWidget(self.label)

        self.budget_input = QLineEdit(self)
        self.budget_input.setPlaceholderText("請輸入預算上限")
        layout.addWidget(self.budget_input)

        self.save_button = QPushButton("保存", self)
        self.save_button.clicked.connect(self.update_budget_settings)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def show_budget_settings(self, budget: float):
        """
        顯示預算設置
        """
        self.budget_input.setText(str(budget))

    def update_budget_settings(self):
        """
        更新預算設置
        """
        budget_str = self.budget_input.text()
        try:
            budget = float(budget_str)
            # 在這裡添加更新預算設置的邏輯
            print(f"更新預算設置為: {budget} USD")
        except ValueError:
            print("輸入的預算格式不正確，請輸入數字。")
