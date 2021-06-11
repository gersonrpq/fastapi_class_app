from fastapi import APIRouter, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.models.schemas import Profile, DefaultResponse, DeletionResponse
from app.views.crud import add_profile, get_profile, delete_profile, update_profile

profiles_router = APIRouter()
templates = Jinja2Templates(directory='app/templates')


@profiles_router.post('/create', response_model=DefaultResponse, 
                                 status_code=status.HTTP_201_CREATED)
async def add_new_profile(profile: Profile):
    return await add_profile(profile)

@profiles_router.get('/{username}', response_class=HTMLResponse,
                                    status_code=status.HTTP_200_OK)
async def get_profile_info(request: Request, username: str):
    profile = await get_profile(username)
    if profile:
        return templates.TemplateResponse('index.html', {'request': request, **profile.to_dict()})
    else:
        request.status_code = status.HTTP_404_NOT_FOUND
        return templates.TemplateResponse('404.html', {'request': request})

@profiles_router.delete('/{username}', response_model=DeletionResponse,
                                        status_code=status.HTTP_200_OK)
async def delete_profile_info(username: str):
    await delete_profile(username)
    return DeletionResponse(message='Profile has been deleted')

@profiles_router.put('/update', response_model=DefaultResponse, 
                                status_code=status.HTTP_200_OK)
async def update_profile_info(profile: Profile):
    return await update_profile(profile.to_dict())    
