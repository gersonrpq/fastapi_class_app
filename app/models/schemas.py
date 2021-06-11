from pydantic import BaseModel, validator, EmailStr, HttpUrl
from typing import Dict, Optional

from app.models.schemas_utils import (
                                        lenght_validation, 
                                        link_construction_check)

TWITTER_PREFFIX = 'https://twitter.com/'
LINKEDIN_PREFFIX = 'https://www.linkedin.com/in/'
PLATZI_PREFFIX = 'https://platzi.com/p/'
GITHUB_PREFFIX = 'https://github.com/'

class Profile(BaseModel):
    username: str
    first_name: str
    last_name: str
    image: Optional[HttpUrl] = 'https://picsum.photos/200'
    twitter: Optional[HttpUrl] = 'https://placeholder.test'
    linkedin: Optional[HttpUrl] = 'https://placeholder.test'
    platzi: Optional[HttpUrl] = 'https://placeholder.test'
    github: Optional[HttpUrl] = 'https://placeholder.test'
    email: Optional[EmailStr] = 'https://placeholder.test'

    @validator('username')
    def appropiate_username_lenght(cls, value):
        return lenght_validation('username', 20, value)
        
    @validator('first_name')
    def appropiate_first_name_lenght(cls, value):
        return lenght_validation('first_name', 20, value)

    @validator('last_name')
    def appropiate_last_name_lenght(cls, value):
        return lenght_validation('last_name', 20, value)

    @validator('twitter')
    def check_twitter_profile_link(cls, value):
        return link_construction_check(TWITTER_PREFFIX, value)

    @validator('linkedin')
    def check_linkedin_profile_link(cls, value):
        return link_construction_check(LINKEDIN_PREFFIX, value)

    @validator('platzi')
    def check_platzi_profile_link(cls, value):
        return link_construction_check(PLATZI_PREFFIX, value)

    @validator('github')
    def check_github_profile_link(cls, value):
        return link_construction_check(GITHUB_PREFFIX, value)
    
    def to_dict(self) -> dict:
        base_dict = {}
        for key, values in self.dict().items():
            base_dict[key] = str(values)
        return base_dict


    class Config:
        schema_extra = {
            'example':  {
                    "username": "pamelavirtual",
                    "first_name": "Pamela",
                    "last_name": "Aristiguieta",
                    "twitter": "https://twitter.com/pamelita",
                    "linkedin": "https://www.linkedin.com/in/pamelavirtual/",
                    "platzi": "https://platzi.com/p/pamelita/",
                    "github": "https://github.com/pamelavirtual",
                    "email": "pamela@organization.com"
                        }
                    }


class DefaultResponse(BaseModel):
    message: str
    profile: Profile

class DeletionResponse(BaseModel):
    message: str
