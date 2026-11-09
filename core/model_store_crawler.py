import requests
from typing import List, Dict, Optional

class ModelStoreCrawler:
    """
    ModelStoreCrawler: 用于从 Hugging Face Hub 和 Civitai v1 API 获取模型信息的类
    """

    def __init__(self, hf_token: Optional[str] = None, civitai_token: Optional[str] = None):
        """
        初始化 ModelStoreCrawler 类

        :param hf_token: Hugging Face Hub API 令牌
        :param civitai_token: Civitai v1 API 令牌
        """
        self.hf_token = hf_token
        self.civitai_token = civitai_token

    def fetch_models(self, hf_repo: str, civitai_category: str) -> List[Dict]:
        """
        从 Hugging Face Hub 和 Civitai v1 API 获取模型信息

        :param hf_repo: Hugging Face Hub 仓库名称
        :param civitai_category: Civitai v1 分类名称
        :return: 模型信息列表
        """
        hf_models = self._fetch_hf_models(hf_repo)
        civitai_models = self._fetch_civitai_models(civitai_category)
        return hf_models + civitai_models

    def parse_model_info(self, model_info: Dict) -> Dict:
        """
        解析模型信息

        :param model_info: 模型信息字典
        :return: 解析后的模型信息字典
        """
        # 这里可以根据需要解析模型信息
        return model_info

    def save_models(self, models: List[Dict], save_path: str) -> None:
        """
        保存模型信息到文件

        :param models: 模型信息列表
        :param save_path: 保存路径
        """
        with open(save_path, 'w') as f:
            for model in models:
                f.write(f"{model}\n")

    def _fetch_hf_models(self, repo: str) -> List[Dict]:
        """
        从 Hugging Face Hub 获取模型信息

        :param repo: Hugging Face Hub 仓库名称
        :return: 模型信息列表
        """
        url = f"https://huggingface.co/api/models/{repo}"
        headers = {"Authorization": f"Bearer {self.hf_token}"} if self.hf_token else {}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def _fetch_civitai_models(self, category: str) -> List[Dict]:
        """
        从 Civitai v1 获取模型信息

        :param category: Civitai v1 分类名称
        :return: 模型信息列表
        """
        url = f"https://civitai.com/api/v1/models?category={category}"
        headers = {"Authorization": f"Bearer {self.civitai_token}"} if self.civitai_token else {}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
