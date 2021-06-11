
import aiohttp

async def generate_random_image() -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get('https://picsum.photos/200') as response:
            pass
    return str(response.url)

def lenght_validation(field_name: str, max_lenght: int, value: str) -> str:
    if len(value) > max_lenght:
        raise ValueError(f'Field {field_name} must have a lenght lower than 20 characthers')
    return value

def link_construction_check(preffix: str, value: str) -> str:
    if preffix not in value and value is not None and value != 'https://placeholder.test':
        value = preffix + value
    return value



