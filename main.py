from TikTokLive import TikTokLiveClient
from TikTokLive.events import CommentEvent, LikeEvent, GiftEvent, FollowEvent
import minecraft as mc
import asyncio

client = TikTokLiveClient(unique_id="@044.puma")

@client.on(CommentEvent)
async def on_comment(event: CommentEvent):
    nickname = event.user_info.nick_name
    comment = event.comment
    mc.tell(f"§l{mc.random_color()}[{nickname}] §f -> {comment}")
    mc.chat_commands(comment)

@client.on(LikeEvent)
async def on_like(event: LikeEvent):
    mc.likes += 1
    mc.like_event()
    nickname = event.user.nick_name
    mc.tell(f"§4[🩷]§l§f{nickname}§4[🩷]")

@client.on(FollowEvent)
async def on_follow(event):
    nickname = event.user.nick_name
    mc.title(f"Follow from {mc.random_color()}{nickname}!")
    mc.play_sound("entity.player.levelup")

def gift(nickname, gift_name, gift_count):
    mc.title(f"{mc.random_color()}{nickname} §fgifted {gift_name} x{gift_count}")
    mob = mc.gift_rewards["default"]
    for g, m in mc.gift_rewards.items():
        if g.lower() in gift_name:
            mob = m
            mc.spawn_mobs(mob, gift_count)

@client.on(GiftEvent)
async def on_gift(event: GiftEvent) :
    nickname = event.user.nick_name
    gift_name = event.gift.name.lower()
    gift_count = event.gift.combo
    gift(nickname, gift_name, gift_count)
    mc.play_sound("entity. firework_rocket.launch")

try:
    client.run()
except KeyboardInterrupt:
    print("Stopping client...")
    try:
        asyncio.run(client.disconnect())
    except Exception:
        pass