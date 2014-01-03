"""
Minecraft Platform Game
v0.1 Les Pounder 2/Jan/2014
Created for PC Format Bookazine
"""
import time
import minecraft.minecraft as minecraft
import minecraft.block as block

mc = minecraft.Minecraft.create()
mc.postToChat("Welcome to the game")
time.sleep(5)

playerPos = mc.player.getPos()
mc.player.setPos(playerPos.x 0, playerPos.y 0, playerPos.z 0)
mc.postToChat("Get to the top of the platforms")
time.sleep(5)

mc.setBlocks(playerTilePos.x - 5, playerTilePos.y - 1, playerTilePos.z - 5, playerTilePos.x + 5, playerTilePos.y -1, playerTilePos.z + 5, block.DIAMOND_BLOCK)

"""
I want platforms to be staggered, around 2 blocks apart and 1 block high, with 1 block between each level
"""