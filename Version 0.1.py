from livewires.beginners import*
from random import *
import time
from random import randrange

screen.set_size(2560,1440),


###########################
###class enemy#############
class Start(Sprite):
    isTouched = False


    def made(self):
        made = mouse.is_pressed(0)
        if mouse.x < self.right and mouse.x > self.left and mouse.y < self.bottom and mouse.y > self.top and made:
            self.isTouched = True
            print "obj has been clicked"
    def eliminate(self):
        self.x = -500

class Enemy(Sprite):

    isClicked = False
    isTouchingWall = False

    def __str__(self):
        return "enemy"

    def click(self):
        click = mouse.is_pressed(0)
        if mouse.x < self.right and mouse.x > self.left and mouse.y < self.bottom and mouse.y > self.top and click:
            self.isClicked = True
            print "obj has been clicked"

    def kill(self):
        self.erase()
        self.x = -500
        self.y = -500


    def wallTouched(self):
        if enemy.x >  screen.width or enemy.x < -50 or enemy.y < -50 or enemy.y > screen.height:
            self.isTouchingWall = True



###########################

screen.background = "AssetBackground.png"
tank = Sprite(image = "AssetBase.png", x=1280, y=720)
deadtank = Sprite(image = "AssetBaseDead.png", x=1280, y=720)
start = Start(image= "AssetStart.png", x=1280, y=720)
score = Text(value=0,size=100,color=white,x=2500,y=60)
enemy1 = Enemy(image="AssetEnemy.png", x=randrange(screen.width), top=0, dy=2, angle=180)
enemy2 = Enemy(image="AssetEnemy.png", x=randrange(screen.width), top=0, dy=3, angle=180)
enemy3 = Enemy(image="AssetEnemy.png", y=randrange(screen.height), left=0, dx=3, angle=270)
enemy4 = Enemy(image="AssetEnemy.png", y=randrange(screen.height), right=0, dx=3, angle=90)
music.track = "SoundEnd.wav"
game = Text(value="You Died",size=300, color=white, x=1280,y=200)
win = Text(value="You Won",size=300, color=white, x=1280,y=200)
play = Text(value="Play?", size= 100, color= blue, x= screen.width/2, y= screen.height/2)
close = Text(value="Quit?", size= 100, color= blue, x=screen.width/2, y= screen.height - 100)
logo = Text(value= "TANK vs NAZIS", size= 120, color= green, x=screen.width/2, y= screen.height - 350)
sound = Sound("SoundGun.wav")




playing = True
music.play()


starts =[]
starts.append(start)
enemies =[]
enemies.append(enemy1)





while playing:







    tank.erase()
    score.erase()
    start.erase()
    deadtank.erase()






    for enemy in enemies:
        enemy.erase()

    for enemy in enemies:
        enemy.y += enemy.dy

    for enemy in enemies:
        enemy.x += enemy.dx


    for enemy in enemies:

        enemy.click()
        enemy.wallTouched()
        # how new enemy is created
        if enemy.isClicked:
            enemy.kill()
            score.value += 1
            enemies.remove(enemy)
            new_enemy1 = Enemy(image="AssetEnemy.png", x=randrange(screen.width), top=0, dy=randrange(2, 3), angle=180)
            new_enemy2 = Enemy(image="AssetEnemy.png", x=randrange(screen.width), bottom=1440, dy=-2, angle=360)
            enemies.append(new_enemy1)
            enemies.append(new_enemy2)
            time.sleep(0.05)
            if score.value > 20:
               new_enemy3 = Enemy(image="AssetEnemy.png", y=randrange(screen.height), right=2560, dx=-2, angle=270)
               new_enemy4 = Enemy(image="AssetEnemy.png", y=randrange(screen.height), left=0, dx=2, angle=90)
               enemies.append(new_enemy3)
               enemies.append(new_enemy4)






        if enemy.isTouchingWall:
            print "wall touched"
            enemies.remove(enemy)
            if score.value < 5:
                new_enemy1 = Enemy(image="AssetEnemy.png", x=randrange(screen.width), top=0, dy=randrange(2, 3), angle=180)
                enemies.append(new_enemy1)








        enemy.draw()








    for enemy in enemies:
        enemy.draw()
        score.draw()
        tank.draw()







    for enemy in enemies:



        if tank.overlaps(enemy):
            game.draw()
            tank.erase()
            music.stop()
            music.track = "SoundExplosion.wav"
            music.play()
            deadtank.draw()
            playing = False


    if score.value > 50:
        win.draw()
        tank.erase()
        music.stop()
        music.track = "SoundExplosion.wav"
        music.play()
        playing = False



    screen.update()
while not keyboard.is_pressed(K_ESCAPE):
    screen.update()
