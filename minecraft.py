from art import tprint

tprint("hahaha", "modular")
tprint("v.0", "modular")

from mcrcon import MCRcon
import random as r

gift_rewards = {
    "rose": "zombie",
    "tiktok": "skeleton",
    "cap": "wither_skeleton",
    "perfume": "wither",
    "heart": "creeper",
    "default": "zombie"
}

likes = 0

mcr = MCRcon("localhost", "robocode")

def execute(command):
    mcr.connect()
    mcr.command(command)
    mcr.disconnect()

def tell(text):
    execute(f'tellraw @a "{text}"')
    
def title(text):
    execute('title @a title {"text":"%s"}' % text)
    
def play_sound(sound_name):
    execute(f'execute at @a run playsound minecraft:{sound_name} master @a')
    
def random_color():
    return f"§{r.randint(0,9)}"

def summon(mob_name):
    execute(f"execute at @a run summon minecraft:{mob_name} ~ ~ ~")

def spawn_mobs(mob_name, count) :
    for _ in range(count):
        summon (mob_name)

def give(item, count=1):
    execute(f"give @a minecraft:{item} {count}")
    
def like_event():
    if likes % 5 == 0:
        give("golden_apple")    
        
def chat_commands(comment):
    match comment:
        case "!zombie": summon("zombie")
        case "!skeleton": summon("skeleton")
        case "!diamond": summon("diamond")
        case "!totem": summon("totem_of_undying")
        case _: pass