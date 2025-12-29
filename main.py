import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# 从系统环境变量获取敏感信息
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION_STR = os.environ.get("SESSION_STR")
# 这里的 ID 就是你之前找到的那个
CHAT_ID = -1002213793309
MESSAGE = "签到"

async def main():
    # 使用 StringSession 登录，无需生成本地文件
    client = TelegramClient(StringSession(SESSION_STR), API_ID, API_HASH)
    await client.start()
    
    try:
        await client.send_message(CHAT_ID, MESSAGE)
        print(f"成功发送消息到 {CHAT_ID}")
    except Exception as e:
        print(f"发送失败: {e}")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
