import torch
import pynvml
from typing import Dict, Optional

class NvidiaProfiler:
    """
    NvidiaProfiler: GPU 自適應引擎的基礎架構
    """

    def __init__(self):
        """
        初始化 GPU 資訊
        """
        self.device_properties = None

    def initialize(self) -> None:
        """
        初始化 GPU 資訊
        """
        pynvml.nvmlInit()
        device_count = pynvml.nvmlDeviceGetCount()
        self.device_properties = [pynvml.nvmlDeviceGetProperties(i) for i in range(device_count)]

    def get_device_info(self) -> Dict:
        """
        獲取 GPU 資訊
        """
        if self.device_properties is None:
            self.initialize()
        return self.device_properties

    def configure_precision(self) -> None:
        """
        配置運算精度
        """
        device_info = self.get_device_info()
        for device in device_info:
            cc = device.computeCapability
            if cc == 7.5:
                # GTX 16 / RTX 20 系列
                torch.set_default_tensor_type(torch.float16)
            elif cc == 8.6:
                # RTX 30 系列
                torch.set_default_tensor_type(torch.bfloat16)
            elif cc >= 8.9:
                # RTX 40 / 50 系列
                torch.set_default_tensor_type(torch.float8)

    def configure_memory_management(self) -> None:
        """
        配置記憶體管理
        """
        device_info = self.get_device_info()
        for device in device_info:
            vram = device.totalMemory
            if vram <= 6 * 1024 * 1024 * 1024:
                # LOW_VRAM (4GB~6GB)
                torch.cuda.set_device(0)
                torch.cuda.empty_cache()
            elif vram <= 12 * 1024 * 1024 * 1024:
                # MID_VRAM (8GB~12GB)
                torch.cuda.set_device(0)
                torch.cuda.empty_cache()
            else:
                # HIGH/ULTRA_VRAM (16GB~24GB+)
                torch.cuda.set_device(0)
                torch.cuda.empty_cache()
