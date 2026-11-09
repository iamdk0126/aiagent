from typing import List, Optional

class AssetContainerNode:
    """
    角色(藍)/場景(綠)/道具(黃) 資產容器與 PC 拖放沙盒上傳
    """

    def __init__(self, asset_type: str, asset_name: str, asset_path: str):
        """
        初始化 AssetContainerNode 类
        :param asset_type: 質產類型 (角色/場景/道具)
        :param asset_name: 質產名稱
        :param asset_path: 質產路徑
        """
        self.asset_type = asset_type
        self.asset_name = asset_name
        self.asset_path = asset_path
        self.assets = []

    def add_asset(self, asset: str) -> None:
        """
        添加資產
        :param asset: 質產
        """
        self.assets.append(asset)

    def remove_asset(self, asset: str) -> None:
        """
        移除資產
        :param asset: 質產
        """
        if asset in self.assets:
            self.assets.remove(asset)

    def get_assets(self) -> List[str]:
        """
        獲取所有資產
        :return: 質產列表
        """
        return self.assets

    def get_asset_info(self, asset_name: str) -> Optional[str]:
        """
        獲取指定資產的資訊
        :param asset_name: 質產名稱
        :return: 質產資訊
        """
        for asset in self.assets:
            if asset_name in asset:
                return asset
        return None

    def sort_assets(self) -> None:
        """
        質產排序
        """
        self.assets.sort()

    def classify_assets(self, category: str) -> List[str]:
        """
        質產分類
        :param category: 分類
        :return: 分類後的資產列表
        """
        return [asset for asset in self.assets if category in asset]

    def search_assets(self, keyword: str) -> List[str]:
        """
        質產搜索
        :param keyword: 搜尋關鍵字
        :return: 搜尋結果
        """
        return [asset for asset in self.assets if keyword in asset]
