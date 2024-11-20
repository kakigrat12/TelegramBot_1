import httpx

# Ваш API-ключ
API_TOKEN = "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"

# Эндпоинт модели
url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"


async def get_image(prompt, finder_id):
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    payload = {"inputs": prompt}

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            with open(f"content/generated_image{finder_id}.png", "wb") as f:
                f.write(response.content)
                return f.name
        else:
            print("Ошибка:", response.json())
