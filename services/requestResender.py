import asyncio


class RequestResender:
    def __init__(self, max_count, delay, timeout):
        self.max_count = max_count
        self.delay = delay
        self.timeout = timeout

    async def start_requests(self, func, *params):
        for i in range(self.max_count):
            print(i, "Попытка отправить запрос...")
            try:
                result = await asyncio.wait_for(func(*params), timeout=self.timeout)
                if result is not None:
                    return result
            except asyncio.TimeoutError:
                print(i, "Время ожидания запроса истекло.")
            except Exception as e:
                print(i, f"Запрос завершился с ошибкой: {e}")

            print(i, "Повтор попытки...")
            await asyncio.sleep(self.delay)

        return None
