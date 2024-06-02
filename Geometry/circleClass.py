class Circle:
  def __init__(self, r):
    self.radius=r
    self.pi=3.14
  def area(self):
    ar=(self.radius**2)*(self.pi)
    return ar

  def circumference(self):
    return (2*self.pi)*(self.radius)

  def daimeter(self):
      d=2*self.radius

      
