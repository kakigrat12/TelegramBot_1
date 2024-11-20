import asyncio
from contentFinders.imageGeneration import get_image
from contentFinders.soundFinder import get_sound
from services.requestResender import RequestResender


class Service:
    user_id = 0

    def __init__(self, user_id):
        self.user_id = user_id

    async def get_image(self, promt):
        resender = RequestResender(5, 1, 5)
        return await resender.start_requests(get_image, promt, self.user_id)

    async def get_sound(self, sound_name):
        resender = RequestResender(5, 3, 5)
        return await resender.start_requests(get_sound, sound_name, self.user_id)


#s = Service(10)
#print(asyncio.run(s.get_sound('sport car')))
