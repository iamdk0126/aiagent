# database/project_assets.py
from typing import List, Dict, Optional
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class ProjectAssets(Base):
    __tablename__ = 'project_assets'
    
    id = Column(Integer, primary_key=True)
    project_id = Column(String, ForeignKey('projects.project_id'), nullable=False)
    asset_type = Column(String, nullable=False)
    asset_path = Column(String, nullable=False)
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)
    
    project = relationship("Project", back_populates="assets")

class Project(Base):
    __tablename__ = 'projects'
    
    project_id = Column(String, primary_key=True)
    project_name = Column(String, nullable=False)
    format_preset_id = Column(String, nullable=False)
    aspect_ratio = Column(String, default='21:9')
    target_resolution = Column(String, default='1920x800')
    fps = Column(Integer, default=24)
    global_lut_path = Column(String)
    default_cjk_font_path = Column(String)
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)
    
    assets = relationship("ProjectAssets", back_populates="project")

# database/asset_embeddings.py
from typing import List, Dict, Optional
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class AssetEmbeddings(Base):
    __tablename__ = 'asset_embeddings'
    
    id = Column(Integer, primary_key=True)
    asset_id = Column(Integer, ForeignKey('project_assets.id'), nullable=False)
    embedding_data = Column(String, nullable=False)
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)
    
    asset = relationship("ProjectAssets", back_populates="embeddings")

# database/db_manager.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .project_assets import Base, ProjectAssets, Project
from .asset_embeddings import AssetEmbeddings

class DBManager:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url, connect_args={"check_same_thread": False})
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    
    def get_session(self):
        return self.Session()

# database/project_archiver.py
from sqlalchemy.orm import sessionmaker
from .db_manager import DBManager
from .project_assets import ProjectAssets, Project
from .asset_embeddings import AssetEmbeddings

class ProjectArchiver:
    def __init__(self, db_url: str):
        self.db_manager = DBManager(db_url)
    
    def create_archive(self, project_id: str, snapshot_data: str):
        session = self.db_manager.get_session()
        project = session.query(Project).filter_by(project_id=project_id).first()
        if project:
            project_assets = session.query(ProjectAssets).filter_by(project_id=project_id).all()
            asset_embeddings = session.query(AssetEmbeddings).filter_by(asset_id=project_assets[0].id).all()
            # Save project, assets, and embeddings to archive_log
            pass
    
    def restore_archive(self, project_id: str, snapshot_data: str):
        session = self.db_manager.get_session()
        # Restore project, assets, and embeddings from archive_log
        pass
