import pyrogram
import logging
import os
from config import Config

class AutoCaptionBotV1(pyrogram.Client):

   

    def __init__(self):
        super().__init__(
            name="Captioner",
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            workers=20,
            plugins=dict(
                root="Plugins"
            )
        )

if __name__ == "__main__":
    autocaption().run()
