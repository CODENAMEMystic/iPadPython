# coding: utf-8

from scene import *
import sound
from math import sin, cos, pi, ceil
from random import uniform as rnd, choice, randint

from colorsys import hsv_to_rgb
import sys
A = Action

def _cmp(a, b):
	return ((a>b)-(a<b))

if sys.version_info[0] >= 3:
	cmp = _cmp
	
nBallX = 1
nBallY = 2

balls_per_second = .5

spawn_interval = balls_per_second*60

paddle_speed = 30
min_ball_speed = 10
max_ball_speed = 18
# How much faster the ball gets when it hits a brick:
brick_speedup = 0.15
# How much faster the ball gets when a new level is reached:
level_speedup = 2.0
powerup_chance = 0.1
filter_names = ['None', 'Gray', 'B&W', 'LCD', 'Wavy']

# Helper functions for collision testing:
def closest_point(rect, circle):
	return Point(max(rect.min_x, min(rect.max_x, circle.x)), max(rect.min_y, min(rect.max_y, circle.y)))

def hit_test(rect, circle, radius, bbox=None):
	if bbox and not rect.intersects(bbox):
		return False
	return abs(closest_point(rect, circle) - circle) < radius

# Particle effect when the ball hits a brick:

# Simple SpriteNode subclasses for the different game objects:

class Ball (SpriteNode):
	def __init__(self, v=(0, 0), r=11, *args, **kwargs):
		SpriteNode.__init__(self, 'pzl:BallBlue', *args, **kwargs)
		self.size = (r*2, r*2)
		self.v = Vector2(*v)
		self.r = r
		self.ball_speed = 10.0
		self.last_collision = None
		self.is_new = False
		self.powerup_type = 0
	
	
# The actual game logic:

class Game (Scene):
	def setup(self):
		self.filter = 0
		self.score = 0
		self.level = 0
		self.paddle_powerup = 0
		self.paddle_charge = 0
		self.lives_left = 3
		self.level_start_time = 0
		self.bricks = []
		self.balls = []
		self.powerups = []
		self.ball_r = 11 if self.size.w > 760 else 7
		# Lower ball speed on iPhone (everything is smaller):
		self.speed_scale = 1.0 if self.size.w > 760 else 0.65
		self.tick = 0
		
		
		
		self.top_bg = SpriteNode(parent=self, position=(0, self.size.h))
		self.top_bg.color = '#1c1c1c'
		self.top_bg.size = self.size.w, 90
		self.top_bg.anchor_point = (0, 1)
		
		self.top_bg = SpriteNode(parent=self, position=(0, self.size.h))
		self.top_bg.color = '#f0f'
		self.top_bg.size = 90, 90
		self.top_bg.anchor_point = (0, 1)
		
		
		
		self.score_label = LabelNode('0', font=('Avenir Next', 40), position=(self.size.w/2, self.size.h-50), parent=self)
		right_wall = Rect(self.size.w, 0, 100, self.size.h)
		left_wall = Rect(-100, 0, 100, self.size.h)
		top_wall = Rect(0, self.size.h, self.size.w, 100)
		bottom_wall = Rect(0, 0, self.size.w, 0)
		self.walls = [SpriteNode(position=rect.center(), size=rect.size) for rect in (left_wall, right_wall, top_wall, bottom_wall)]
		self.background_color = '#292e37'
		
		self.new_game()

	def new_game(self):
		self.level = 0
		for b in self.balls:
			b.remove_from_parent()
		self.balls = []
		self.spawn_ball()
	
	
	def update(self):
		self.update_all_balls()
		
		#if self.tick % spawn_interval == 0:
			#self.spawn_ball()
		#self.tick += 1

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
		colliders = self.bricks + self.walls
		ball_bbox = Rect(bp.x-ball_r, bp.y-ball_r, ball_r*2, ball_r*2)
		collisions = []
		new_ball = ball.is_new
		for node in colliders:
			if new_ball:
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
		####
				
		ball.position = bp
		ball.is_new = False
		ball.v = (v/abs(v)) * ball.ball_speed * self.speed_scale
	
	def spawn_ball(self):
		new_ball = Ball(r=self.ball_r, v=(nBallX, nBallY), position=(self.size.w/2, self.size.h/2), parent=self)
		new_ball.scale = 0
		new_ball.run_action(A.scale_to(1, 0.3))
		new_ball.ball_speed = min(max_ball_speed, min_ball_speed + level_speedup * self.level)
		self.balls.append(new_ball)
	
	def touch_began(self, touch):
		x, y = touch.location
		if x < 90 and y > self.size.h - 90:
			self.spawn_ball()
			#if self.paused:
				#self.paused = False
			#else:
				#self.paused = True
		
		
	
	def touch_moved(self, touch):
		pass
	
	

# Run the game:
if __name__ == '__main__':
	run(Game(), show_fps=False)