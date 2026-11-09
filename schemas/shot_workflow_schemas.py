from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class Project(BaseModel):
    """
    Project: 專案資料模型
    """
    project_id: str = Field(..., description="專案ID")
    project_name: str = Field(..., description="專案名稱")
    description: Optional[str] = Field(None, description="專案描述")
    created_at: str = Field(..., description="創建時間")
    updated_at: str = Field(..., description="更新時間")

class Episode(BaseModel):
    """
    Episode: 剧集資料模型
    """
    episode_id: str = Field(..., description="劇集ID")
    episode_name: str = Field(..., description="劇集名稱")
    project_id: str = Field(..., description="專案ID")
    description: Optional[str] = Field(None, description="劇集描述")
    created_at: str = Field(..., description="創建時間")
    updated_at: str = Field(..., description="更新時間")

class Asset(BaseModel):
    """
    Asset: 素材資料模型
    """
    asset_id: str = Field(..., description="素材ID")
    asset_name: str = Field(..., description="素材名稱")
    asset_type: str = Field(..., description="素材類型")
    episode_id: str = Field(..., description="劇集ID")
    description: Optional[str] = Field(None, description="素材描述")
    created_at: str = Field(..., description="創建時間")
    updated_at: str = Field(..., description="更新時間")

class Shot(BaseModel):
    """
    Shot: 分鏡資料模型
    """
    shot_id: str = Field(..., description="分鏡ID")
    shot_name: str = Field(..., description="分鏡名稱")
    episode_id: str = Field(..., description="劇集ID")
    asset_id: str = Field(..., description="素材ID")
    start_frame: int = Field(..., description="起始帧")
    end_frame: int = Field(..., description="結束帧")
    description: Optional[str] = Field(None, description="分鏡描述")
    created_at: str = Field(..., description="創建時間")
    updated_at: str = Field(..., description="更新時間")

class Checkpoint(BaseModel):
    """
    Checkpoint: 檢查點資料模型
    """
    checkpoint_id: str = Field(..., description="檢查點ID")
    shot_id: str = Field(..., description="分鏡ID")
    checkpoint_data: bytes = Field(..., description="檢查點數據")
    created_at: str = Field(..., description="創建時間")
    updated_at: str = Field(..., description="更新時間")

class AssetEmbedding(BaseModel):
    """
    AssetEmbedding: 資產嵌入向量資料模型
    """
    embedding_id: str = Field(..., description="嵌入向量ID")
    asset_id: str = Field(..., description="素材ID")
    embedding_vector: List[float] = Field(..., description="嵌入向量")
    created_at: str = Field(..., description="創建時間")
    updated_at: str = Field(..., description="更新時間")
