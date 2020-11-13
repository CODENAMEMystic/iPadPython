from scene import *
import sound, console
import random
from math import sin, cos, pi, ceil
A = Action
console.clear()
def _cmp(a, b):
	return ((a>b)-(a<b))
if sys.version_info[0] >= 3:
	cmp = _cmp
	
class Ball (SpriteNode):
	def __init__(self, v=(0, 0), r=11, *args, **kwargs):
		SpriteNode.__init__(self, 'pzl:BallBlue', *args, **kwargs)
		self.size = (r*2, r*2)
		self.v = Vector2(*v)
		self.r = r
		self.ball_speed = 10.0
		self.last_collision = None
		
		
		
min_ball_speed = 5
max_ball_speed = 10

def closest_point(rect, circle):
	return Point(max(rect.min_x, min(rect.max_x, circle.x)), max(rect.min_y, min(rect.max_y, circle.y)))
def hit_test(rect, circle, radius, bbox=None):
	if bbox and not rect.intersects(bbox):
		return False
	return abs(closest_point(rect, circle) - circle) < radius

class MyScene (Scene):
	def setup(self):
		self.background_color = '#550055'
		self.balls = []
		self.ball_r = 11
		
		right_wall = Rect(self.size.w, 0, 100, self.size.h)
		left_wall = Rect(-100, 0, 100, self.size.h)
		top_wall = Rect(0, self.size.h-90, self.size.w, 100)
		self.walls = [SpriteNode(position=rect.center(), size=rect.size) for rect in (left_wall, right_wall, top_wall)]
		
		self.spawn_ball()
	
	
		
			
	def did_change_size(self):
		pass
	
	def update(self):
		self.update_all_balls()
	
	def update_all_balls(self):
		for ball in list(self.balls):
			# Update in multiple steps, so a ball cannot pass through a brick in a single frame:
			steps = int(ceil(abs(ball.v)/5.0))
			for i in range(steps):
				self.update_ball(ball, ball.v / steps)
			if ball.position.y < -50:
				self.balls.remove(ball)
				ball.remove_from_parent()
	
	def update_ball(self, ball, v):
		bp = ball.position + v
		ball_r = ball.r
		colliders = self.walls
		ball_bbox = Rect(bp.x-ball_r, bp.y-ball_r, ball_r*2, ball_r*2)
		collisions = []
		
		new_ball = ball.is_new
		for node in colliders:
			if new_ball and node != self.paddle:
				continue
			if node == ball.last_collision:
				continue
			frame = node.frame
			
			if hit_test(frame, bp, ball_r, ball_bbox):
				collisions.append((frame, node))
		if not collisions:
			ball.position = bp
			return
		# Move the ball back where it came from until it doesn't collide anymore:
		while any(hit_test(c[0], bp, ball_r) for c in collisions):
			bp -= (v / abs(v))
		# Find the closest collision point:
		collisions = [(c[1], closest_point(c[0], bp)) for c in collisions]
		sorted_collisions = sorted(collisions, key=lambda x: abs(x[1] - bp))
		collider, p = sorted_collisions[0]
		
		
		ball.last_collision = collider
		side_hit = abs(v.x) > 0 and cmp(bp.x - collider.position.x, 0) != cmp(v.x, 0) and abs(bp.x - p.x) > abs(bp.y - p.y)
		v *= (-1, 1) if side_hit else (1, -1)
		
	
	def spawn_ball(self):
		new_ball = Ball(r=self.ball_r, v=(5, 2), position=(self.size.w/2, self.size.h/2), parent=self)
		new_ball.scale = 0
		new_ball.run_action(A.scale_to(1, 0.3))
		new_ball.ball_speed = min(max_ball_speed, min_ball_speed)
		new_ball.is_new = False
		self.balls.append(new_ball)
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=False)