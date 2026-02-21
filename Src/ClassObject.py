import matplotlib.pyplot as plt
#matplotlib inline
class Circle(object):
    #Constructor
    def __init__(self, radius, color):
        self.radius = radius;
        self.color = color;
    #Method to include rafidus
    def add_radius(self, r):
        self.radius += r
        return self.radius
    
    def draw_circle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()
Redcircle = Circle(10, 'green')
Redcircle.draw_circle()


        