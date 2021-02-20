import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep

mc = minecraft.Minecraft.create()

def iceHands():
    for hit in mc.events.pollBlockHits():
        mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.ICE)

def snowFeet():
    sleep(0.1)
    p = mc.player.getTilePos()
    mc.setBlock(p.x, p.y, p.z, block.SNOW)

def iceHouse():
    p = mc.player.getTilePos()
    mc.setBlocks(p.x + 1, p.y, p.z + 1, p.x + 10, p.y + 5, p.z + 10, block.ICE)
    mc.setBlocks(p.x + 2, p.y + 1, p.z + 2, p.x + 9, p.y + 4, p.z + 9, block.AIR)
    mc.setBlocks(p.x + 5, p.y + 1, p.z + 1, p.x + 6, p.y + 3, p.z + 1, block.AIR)
    mc.setBlocks(p.x + 2, p.y, p.z + 2, p.x + 9, p.y, p.z + 9, block.WOOL.id, 14)

iceHouse()
while True:
    snowFeet()
    iceHands()

