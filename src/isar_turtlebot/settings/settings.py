from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    IMAGE_FILETYPE: str = Field(default="jpg")
    THERMAL_IMAGE_FILETYPE: str = Field(default="png")

    ROS_BRIDGE_HOST: str = Field(default="localhost")
    ROS_BRIDGE_PORT: int = Field(default=9090)

    STORAGE_FOLDER: str = Field(default="./temp_results")
    PUBLISHING_TIMEOUT: int = Field(default=30)
    INSPECTION_POSE_TIMEOUT: int = Field(default=60)
    GET_IMAGE_TIMEOUT: int = Field(default=5)

    class Config:
        env_prefix = "ISAR_TURTLEBOT_"


settings = Settings()
