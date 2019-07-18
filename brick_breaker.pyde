rwidth=100
rheight=50
rect_y=0
ballx=270
bally=200
xspeed=3
yspeed=3
showbox_one= True
showbox_two= True
showbox_three=True
showbox_four=True
showbox_five=True

def setup():
   size (500,500)
   background(200,200,200)
   
def draw():
    global rwidth
    global rheight 
    global rect_y
    global ballx
    global xspeed
    global bally
    global yspeed
    global showbox_one
    global showbox_two
    global showbox_three
    global showbox_four
    global showbox_five
    
    background(0,0,0)
    fill(252, 164, 96)
    rect(mouseX -75, 400,150,30)#paddle

    noStroke() 
    if showbox_one==True:
        fill(167, 252, 224)
        rect(0,rect_y,rwidth,rheight)
    if ballx >0 and ballx<100 and bally<50:
        showbox_one=False
        (random(0,255),random(0,255),random(0,225))
    if showbox_two==True:
        fill(167, 200, 252)
        rect(100,rect_y,rwidth,rheight)
    if ballx >100 and ballx<200 and bally<50:
        showbox_two=False
   
    if showbox_three==True:
        fill(219, 179, 245)
        rect(200,rect_y,rwidth,rheight)
    if ballx >200 and ballx<300 and bally<50:
        showbox_three=False
    
    if showbox_four==True:
        fill(245, 179, 194)
        rect(300,rect_y,rwidth,rheight)
    if ballx >300 and ballx<400 and bally<50:
        showbox_four=False
        
    if showbox_five==True:
        fill(224, 245, 179)
        rect(400,rect_y,rwidth,rheight)
    if ballx >400 and ballx<500 and bally<50:
        showbox_five=False
   
         
    ellipse(ballx,bally,30,30)
    if ballx >0 and ballx<100 and bally<50:
        (random(0,255),random(0,255),random(0,225))

   
    if mouseX<5 :
        xspeed=4 
    if bally>480:
        yspeed=-yspeed
    if bally< 5:
        yspeed=4
    if ballx>450:
        xspeed=-xspeed
    if ballx<5:
        xspeed=4

    if bally> 385 and ballx > mouseX-75 and ballx<mouseX+75:
        yspeed= -yspeed
       

    
    ballx=ballx+xspeed 
    bally= bally+yspeed 
    
        

   
