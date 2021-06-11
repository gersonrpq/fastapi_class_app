from tortoise import fields, models
#from tortoise.contrib.pydantic import pydantic_model_creator

class ProfileModel(models.Model):

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    first_name = fields.CharField(max_length=20)
    last_name = fields.CharField(max_length=20)
    image = fields.CharField(max_length=300, null=True)
    twitter = fields.CharField(max_length=50, null=True)
    linkedin = fields.CharField(max_length=50, null=True)
    platzi = fields.CharField(max_length=50, null=True)
    github = fields.CharField(max_length=50, null=True)
    email = fields.CharField(max_length=50, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.username

#Profile = pydantic_model_creator(ProfileModel, "Profile")