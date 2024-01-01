#(©)Codexbotz

from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
import schedule, time, threading
from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, CHANNEL_ID, PORT

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        if FORCE_SUB_CHANNEL:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot Can't Export Invite Link From Force Sub Channel !!")
                self.LOGGER(__name__).warning(f"Please Double Check The FORCE_SUB_CHANNEL Value And Make Sure Bot Is Admin In Channel With Invite Users Via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL}")
                self.LOGGER(__name__).info("\nBot Stopped...")
                sys.exit()
        try:
            db_channel = await self.get_chat(chat_id=CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure The Bot Is Admin In DB Channel, And Double Check The CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped !!")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.username = usr_bot_me.username
        self.LOGGER(__name__).info(f"@{self.username} Is Live Now ⚡")
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

#        def run_sch():
#            while True:
#                schedule.run_pending()
#                time.sleep(1)
#        rxn = threading.Thread(target=run_sch)
#        rxn.start()
        
#        def run_continuously(interval=1):
#            cease_continuous_run = threading.Event()
#        
#            class ScheduleThread(threading.Thread):
#                @classmethod
#                def run(cls):
#                    while not cease_continuous_run.is_set():
#                        schedule.run_pending()
#                        time.sleep(interval)
#        
#            continuous_thread = ScheduleThread()
#            continuous_thread.start()
#            return cease_continuous_run
#        run_continuously()

        def run_sxh():
            while 1:
                n = schedule.idle_seconds()
                if n is None:
                    n = 1
                if n > 0:
                    time.sleep(n)
                schedule.run_pending()
        rxn = threading.Thread(target=run_sxh)
        rxn.start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot Stopped.")
