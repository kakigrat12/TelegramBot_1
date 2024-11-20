import httpx
import random

# Ваш API-ключ
API_TOKEN = "6vnLrOvN36Dj3qmbde6aUTWeNSec2UCyXtyb06VL"


async def get_sound_from_id(sound_id, finder_id):
    async with httpx.AsyncClient() as client:
        url = f'https://freesound.org/apiv2/sounds/{sound_id}/?token={API_TOKEN}'
        response = await client.get(url)

        if response.status_code == 200:
            sound_data = response.json()
            preview_url = sound_data['previews']['preview-lq-mp3']  # или 'preview-lq-mp3' для mp3

            # Скачать файл
            preview_response = await client.get(preview_url)
            with open(f'content/sound_{finder_id}.mp3', 'wb') as f:
                f.write(preview_response.content)
                return f.name
        else:
            print(f"Ошибка при запросе: {response.status_code}")


async def get_sound(query, finder_id):
    print(query, finder_id)
    async with httpx.AsyncClient() as client:
        search_url = f"https://freesound.org/apiv2/search/text/?query={query}&token={API_TOKEN}"
        search_response = await client.get(search_url)

        if search_response.status_code == 200:
            results = search_response.json().get("results", [])
            if results:
                sound_id = results[random.randint(0, len(results) - 1)]["id"]
                return await get_sound_from_id(sound_id, finder_id)
        else:
            print("Ошибка при поиске:", search_response.json())
