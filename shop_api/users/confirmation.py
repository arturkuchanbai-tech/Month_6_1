import redis
from django.conf import settings

redis_client = redis.Redis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=0,decode_responses=True)

def save_code(user_id: int, code: str):
    key = f"confirmation_code:{user_id}"
    redis_client.setex(key, 300, code)  


def verify_code(user_id: int, input_code: str) -> bool:
    key = f"confirmation_code:{user_id}"
    stored_code = redis_client.get(key)

    if not stored_code:
        return False

    if stored_code == input_code:
        redis_client.delete(key)
        return True
    return False