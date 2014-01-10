import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import threading

time.sleep(2)
mc = minecraft.Minecraft.create()
playerPos = mc.player.getPos()
playerPos = minecraft.Vec3(int(playerPos.x), int(playerPos.y), int(playerPos.z))
#Change the message below to read "Welcome to the game" Step 5 in the magazine.
mc.postToChat("Hello World")
time.sleep(1)
mc.postToChat("Can you reach the top without flying or falling off?")
time.sleep(1)

#The next two lines are for step 6 and relate to our position in the game world.
playerPos = mc.player.getPos()
mc.postToChat(playerPos)
mc.player.setTilePos(0,50,0)
for more in range(0,21):
        mc.setBlock(playerPos.x + more, playerPos.y + more, playerPos.z + more,block.WOOD_PLANKS)
        mc.setBlock(playerPos.x + more +1, playerPos.y + more, playerPos.z + more,block.WOOD_PLANKS)
for up in range(21, 30):
        mc.setBlock(playerPos.x + up + 1, playerPos.y + up, playerPos.z + up, block.DIAMOND_BLOCK)
        mc.setBlock(playerPos.x + up + 2, playerPos.y + up, playerPos.z + up, block.DIAMOND_BLOCK)


mc.postToChat("You have 30 seconds to reach the top")
time.sleep(1)
mc.postToChat("GO")
time.sleep(1)

clock = 30
while clock > 0:
        mc.postToChat(clock)
        time.sleep(1)
        clock = clock - 1

mc.postToChat("Time's up!")
