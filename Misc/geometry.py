from scene import *

class MyScene (Scene):
    def draw(self):
        background('gray')
        colors = ['red', 'green', 'blue', 'yellow','purple']
        # Move to the center of the screen:
        translate(self.size.w/2, self.size.h/2)
        for color in colors:
            # Set the current fill color (this affects the drawing commands that follow)
            fill(color)
            # Rotate the transformation matrix (this is cumulative):
            rotate(-20)
            # Note: The coordinates are relative to the center of the screen because of the previous `translate` command:
            rect(-50, -50, 100, 100)

run(MyScene())
