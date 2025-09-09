
from pydantic import BaseModel, Field


class File(BaseModel):
    path: str = Field(
        description="The path to the file to be created or modified"
    )
    purpose: str = Field(
        description="The purpose of the file, e.g. 'main application logic', 'data processing module',etc. "
    )

class Plan(BaseModel):
    name: str = Field(
        description="The name of app to be"
    )
    description: str = Field(
        description="a online description of the app to be build, e.g. 'A web application for managing person'"
    )
    techstack: str = Field(
        description="The tech stack to be used for the app, e.g. 'python', 'javascript', 'react', 'flask', etc"
    )
    features: list[str] = Field(
        description="A list of features that tha app should have, e.g. 'user authentication', 'data visualization' etc."
    )
    files: list[File] = Field(
        description="A list of files to be created, each with a 'path' and 'purpose' "
    )


class Schema(BaseModel):
    price:float
    eps:float