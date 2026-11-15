import turtle

screen = turtle.Screen()
screen.setup(width=900, height=700)
screen.bgcolor("white")
screen.title("Wireframe Mesh Dragon over Grass and Trees")

t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed so you don't wait 5 minutes
t.pensize(1)


# Function to draw an independent line segment between two points
def line(p1, p2):
  t.penup()
  t.goto(p1)
  t.pendown()
  t.goto(p2)

# Function to draw a connected chain of lines
def polyline(points):
  for i in range(len(points) - 1):
    line(points[i], points[i + 1])


# ==========================================
# 1. LANDSCAPE: HORIZON, GRASS BLADES & TREES
# ==========================================
t.pencolor("darkgreen")

# Ground base lines
line((-420, -220), (420, -220))
line((-420, -225), (420, -225))

# Individual grass tufts across the ground (clusters of angled lines)
for x in range(-400, 401, 20):
  line((x, -220), (x - 6, -202))
  line((x, -220), (x, -198))
  line((x, -220), (x + 6, -204))


# Function to build a wireframe tree out of straight lines
def draw_tree(base_x, base_y, scale):
  # Trunk lines (left, right, bark texture lines, and base)
  t.pencolor("saddlebrown")
  line((base_x - 8 * scale, base_y), (base_x - 5 * scale, base_y + 60 * scale))
  line((base_x + 8 * scale, base_y), (base_x + 5 * scale, base_y + 60 * scale))
  line((base_x - 2 * scale, base_y), (base_x - 1 * scale, base_y + 60 * scale))
  line((base_x + 3 * scale, base_y), (base_x + 2 * scale, base_y + 50 * scale))

  # Branches
  line(
      (base_x - 5 * scale, base_y + 45 * scale),
      (base_x - 25 * scale, base_y + 70 * scale),
  )
  line(
      (base_x + 5 * scale, base_y + 45 * scale),
      (base_x + 25 * scale, base_y + 70 * scale),
  )
  line(
      (base_x, base_y + 55 * scale), (base_x - 15 * scale, base_y + 85 * scale)
  )
  line(
      (base_x, base_y + 55 * scale), (base_x + 15 * scale, base_y + 85 * scale)
  )

  # Tiered pine/leaf canopy made of triangulated line segments
  t.pencolor("forestgreen")
  tiers = [
      (base_y + 50 * scale, 45 * scale, 35 * scale),
      (base_y + 75 * scale, 35 * scale, 30 * scale),
      (base_y + 95 * scale, 22 * scale, 25 * scale),
  ]
  for y_level, half_w, height in tiers:
    top = (base_x, y_level + height)
    left = (base_x - half_w, y_level)
    right = (base_x + half_w, y_level)
    # Outer triangle
    polyline([left, top, right, left])
    # Internal wireframe ribbing for leaves
    line(top, (base_x - half_w * 0.5, y_level))
    line(top, (base_x, y_level))
    line(top, (base_x + half_w * 0.5, y_level))


# Place several trees across the land
draw_tree(-310, -220, 1.3)
draw_tree(-170, -220, 0.9)
draw_tree(80, -220, 1.1)
draw_tree(240, -220, 1.4)
draw_tree(350, -220, 0.8)


# ==========================================
# 2. THE DRAGON (MULTI-LINE WIREFRAME MESH)
# ==========================================
t.pencolor("black")
t.pensize(1.5)

# Top spine points and Bottom belly/chest points (giving the dragon thickness)
spine = [
    (-260, 10),
    (-210, 25),
    (-160, 45),
    (-110, 60),
    (-60, 68),
    (-10, 75),
    (40, 82),
    (85, 105),
    (120, 140),
    (145, 160),
]
belly = [
    (-260, 10),
    (-208, 16),
    (-155, 30),
    (-105, 38),
    (-55, 35),
    (-5, 32),
    (45, 45),
    (95, 80),
    (130, 120),
    (150, 142),
]

# Draw top and bottom body outlines
polyline(spine)
polyline(belly)

# Connect spine and belly with cross-ribbing & diagonal mesh lines (3D body volume)
for i in range(len(spine) - 1):
  line(spine[i], belly[i])  # Vertical rib line
  line(spine[i], belly[i + 1])  # Diagonal truss line 1
  line(belly[i], spine[i + 1])  # Diagonal truss line 2

# Dorsal spikes along the dragon's spine
for i in range(1, len(spine) - 1):
  sx, sy = spine[i]
  next_x, next_y = spine[i + 1]
  spike_tip = (sx - 8, sy + 16)
  line((sx, sy), spike_tip)
  line(spike_tip, ((sx + next_x) / 2, (sy + next_y) / 2))

# Head, Snout, Jaws, Horns, and Teeth (collection of structured lines)
head_top = (145, 160)
snout_tip = (195, 152)
upper_jaw_mid = (170, 144)
mouth_corner = (152, 145)
lower_jaw_tip = (188, 136)
chin = (150, 142)

# Skull & Jaw wireframe
polyline([head_top, (172, 160), snout_tip, upper_jaw_mid, mouth_corner])
polyline([mouth_corner, lower_jaw_tip, chin, head_top])
line(head_top, upper_jaw_mid)
line((172, 160), mouth_corner)
line((160, 154), (170, 156))  # Sharp eye slit

# Teeth lines
line((185, 149), (183, 144))
line((176, 146), (175, 141))
line((180, 138), (181, 143))

# Swept-back Horns (multi-line thickness)
polyline([head_top, (125, 185), (95, 198), (132, 168), head_top])
polyline([(140, 155), (118, 172), (100, 180), (130, 150)])

# Tail Spade (sharp geometric spear at the end of the tail)
polyline([(-260, 10), (-285, 22), (-310, 5), (-280, -4), (-260, 10)])
line((-260, 10), (-310, 5))

# ==========================================
# 3. FOREGROUND & BACKGROUND WINGS (RIBS & MEMBRANE MESH)
# ==========================================
shoulder_top = (15, 78)
shoulder_base = (-25, 68)
wing_elbow = (-15, 175)
wing_wrist = (-75, 245)

# Main Wing Arm Bone (double-lined for bone thickness)
polyline([shoulder_top, wing_elbow, wing_wrist])
polyline([(10, 72), (-22, 170), (-82, 240)])
line(shoulder_top, (10, 72))
line(wing_elbow, (-22, 170))
line(wing_wrist, (-82, 240))

# Wing tip claw
polyline([wing_wrist, (-85, 265), (-95, 250), (-82, 240)])

# 4 Wing Finger Ribs radiating from the wrist
wing_tips = [
    (-220, 230),  # Outer wingtip
    (-190, 165),  # Mid-outer rib tip
    (-135, 115),  # Mid-inner rib tip
    (-75, 85),  # Inner rib tip
]

for tip in wing_tips:
  line(wing_wrist, tip)
  line((-82, 240), tip)  # Double line for rib thickness

# Scalloped trailing edge of the wing membrane + internal webbing lines
membrane_points = wing_tips + [shoulder_base]
for i in range(len(membrane_points) - 1):
  p_start = membrane_points[i]
  p_end = membrane_points[i + 1]
  # Arch midpoint for bat-wing curve made of straight segments
  mid_x = (p_start[0] + p_end[0]) / 2 + 10
  mid_y = (p_start[1] + p_end[1]) / 2 + 12
  polyline([p_start, (mid_x, mid_y), p_end])

  # Structural crease lines inside the wing membrane panels
  line(wing_wrist, (mid_x, mid_y))
  for frac in [0.35, 0.65]:
    r1_x = wing_wrist[0] + (p_start[0] - wing_wrist[0]) * frac
    r1_y = wing_wrist[1] + (p_start[1] - wing_wrist[1]) * frac
    r2_x = wing_wrist[0] + (p_end[0] - wing_wrist[0]) * frac
    r2_y = wing_wrist[1] + (p_end[1] - wing_wrist[1]) * frac
    line((r1_x, r1_y), (r2_x, r2_y))

# Secondary Background Wing (angled behind the main wing for depth)
bg_shoulder = (35, 80)
bg_wrist = (5, 235)
line(bg_shoulder, (25, 165))
line((25, 165), bg_wrist)
bg_tips = [(-110, 255), (-85, 195), (-40, 145), (5, 80)]
for tip in bg_tips:
  line(bg_wrist, tip)
polyline(bg_tips)

# ==========================================
# 4. FRONT & HIND LEGS WITH CLAWS (MULTI-LINE)
# ==========================================
# Hind Leg (hip, thigh, calf, and 3 talons)
hind_hip1, hind_hip2 = (-95, 42), (-70, 40)
hind_knee1, hind_knee2 = (-120, 12), (-102, 10)
hind_ankle1, hind_ankle2 = (-95, -15), (-85, -12)
polyline([hind_hip1, hind_knee1, hind_ankle1])
polyline([hind_hip2, hind_knee2, hind_ankle2])
line(hind_hip1, hind_knee2)
line(hind_knee1, hind_ankle2)
# Hind Claws
for cx, cy in [(-75, -28), (-82, -32), (-92, -30)]:
  polyline([hind_ankle1, (cx, cy), hind_ankle2])

# Front Leg (shoulder, forearm, and 3 talons)
front_sh1, front_sh2 = (35, 50), (55, 55)
front_el1, front_el2 = (18, 18), (32, 20)
front_wr1, front_wr2 = (42, -5), (50, 0)
polyline([front_sh1, front_el1, front_wr1])
polyline([front_sh2, front_el2, front_wr2])
line(front_sh1, front_el2)
line(front_el1, front_wr2)
# Front Claws
for cx, cy in [(65, -15), (58, -22), (48, -20)]:
  polyline([front_wr1, (cx, cy), front_wr2])

t.hideturtle()
turtle.done()