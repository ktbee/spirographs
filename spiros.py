import math
import turtle

class Spiro:
  # constructor
  def __init__(self, xc, yc, col, R, r, l):
    self.t = turtle.Turtle()
    self.t.shape('turtle')
    self.step = 5
    self.drawingComplete = False
    self.setparams(xc, xy, col, R, r, l)

    self.restart()

  def setparams(self, xc, yc, col, R, r, l):
    self.xc = xc
    self.yc = yc
    self.R = int(R)
    self.r = int(r)
    self.l = l
    self.col = col

    """
    reduce r/R by dividing with Greatest Common Denominator.
    This gives us how many rotations we need to finish the spirograph
    """
    gcdVal = gcd(self.r, self.R)
    self.nRot = self.r // gcdVal
    # Get ration of radii
    self.k = r/float(R)
    self.t.color(*col)
    # store the current angle
    self.a = 0

    
