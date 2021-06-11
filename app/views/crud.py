from typing import List 

from app.models.orm_models import ProfileModel
from app.models.schemas import DeletionResponse, Profile, DefaultResponse
from app.models.schemas_utils import generate_random_image


async def add_profile(profile: Profile) -> DeletionResponse:
    image_url = await generate_random_image()
    profile.image = image_url
    new_profile = await ProfileModel.create(**profile.to_dict())
    new_profile = Profile(**dict(new_profile))
    response = DefaultResponse(
                    message='Profile created successfully', 
                    profile = new_profile)
    return response

async def get_profile(username: str) -> Profile:
    profile = await ProfileModel.get_or_none(username=username)
    if profile:
        profile = Profile(**dict(profile))
        return profile

async def delete_profile(username: str) -> None:
    profile = await ProfileModel.get_or_none(username=username)
    if profile is not None:
        await profile.delete()

async def update_profile(profile_data: dict) -> DefaultResponse:
    profile_to_update = await ProfileModel.get_or_none(username=profile_data['username'])
    if profile_to_update:
        for field_name in profile_data:
            setattr(profile_to_update, field_name, profile_data.get(field_name))
        new_image_url = await generate_random_image()
        setattr(profile_to_update, 'image', new_image_url)
        await profile_to_update.save()
        profile_updated = Profile(**dict(profile_to_update))
        return DefaultResponse(
                    message='Profile updated successfully',
                    profile = profile_updated
        )