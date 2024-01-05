import turtle 
  
  
myTurtle = turtle.Turtle() 
myWin = turtle.Screen() 
  
# Turtle to draw a spiral 
def drawSpiral(myTurtle, linelen): 
    myTurtle.forward(linelen) 
    myTurtle.right(90) 
    drawSpiral(myTurtle, linelen+10) 
  
drawSpiral(myTurtle, 0) 
myWin.exitonclick() 