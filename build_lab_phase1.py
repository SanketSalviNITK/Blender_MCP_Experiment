"""
Phase 1 — Clear living room, build Missing Scientist's Lab shell:
  - Room: 5x5x3m dark brick/concrete corner
  - Desk: dark walnut top + brushed aluminum legs
  - Camera: repositioned to face desk corner
  - Lighting: amber desk lamp + cyan monitor glow placeholder
"""
import bpy, math

# ════════════════════════════════════════════════════════════════════════════
# 0. CLEAR LIVING ROOM OBJECTS
# ════════════════════════════════════════════════════════════════════════════
keep = {'SceneCamera', 'RoomFloor', 'RoomWalls'}   # will be created below

remove_names = [
    'AloeVera','PlantPot','DiningTable','SideTable',
    'SideTableLeg_1','SideTableLeg_2','SideTableLeg_3','SideTableLeg_4',
    'TableLeg_1','TableLeg_2','TableLeg_3','TableLeg_4',
    'Shelf_Left','Shelf_Right','Shelf_1','Shelf_2','Shelf_3','Shelf_4',
    'Shelf_Back','Shelf_Bottom','Shelf_Top',
    'Book_S1_1','Book_S1_2','Book_S1_3','Book_S1_4','Book_S1_5','Book_S1_6',
    'Book_S2_1','Book_S2_2','Book_S2_3','Book_S2_4','Book_S2_5','Book_S2_6',
    'Book_S3_1','Book_S3_2','Book_S3_3','Book_S3_4','Book_S3_5',
    'FloorBook_1','FloorBook_2','Candle',
    'CoffeeMug','MugHandle','GlassesCase','LinenNapkin','LoosePaper','RedBook',
    'LampBase','LampPole','LampGlassSphere','DustMotes',
    'PictureFrame','PictureCanvas',
    'StoneWall','Floor',
    'FillLight','LampGlow','RimLight','WindowLight',
]
removed = 0
for name in remove_names:
    obj = bpy.data.objects.get(name)
    if obj:
        bpy.data.objects.remove(obj, do_unlink=True)
        removed += 1
print(f'Removed {removed} living room objects')

# Remove old collections (except Cameras)
for col_name in ['Furniture','DecorativePlant','TableItems','Bookshelf',
                 'Books','ShelfDecorations','Lamp','Lighting','Environment']:
    col = bpy.data.collections.get(col_name)
    if col:
        bpy.data.collections.remove(col)
print('Old collections cleared')

# ════════════════════════════════════════════════════════════════════════════
# 1. HELPER: get or create collection
# ════════════════════════════════════════════════════════════════════════════
def get_col(name, parent=None):
    if name in bpy.data.collections:
        col = bpy.data.collections[name]
    else:
        col = bpy.data.collections.new(name)
    target = parent if parent else bpy.context.scene.collection
    if col.name not in [c.name for c in target.children]:
        target.children.link(col)
    return col

def assign(obj, col):
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    col.objects.link(obj)

col_env      = get_col('Environment')
col_desk     = get_col('Desk')
col_left     = get_col('LeftCluster')
col_right    = get_col('RightCluster')
col_center   = get_col('CenterDesk')
col_cork     = get_col('Corkboard')
col_sacred   = get_col('SacredMeshes')
col_lighting = get_col('Lighting')
col_cameras  = get_col('Cameras')

# ════════════════════════════════════════════════════════════════════════════
# 2. HELPER: make material
# ════════════════════════════════════════════════════════════════════════════
def make_mat(name, color, roughness=0.8, metallic=0.0, emit=0.0):
    if name in bpy.data.materials:
        bpy.data.materials.remove(bpy.data.materials[name])
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes; nodes.clear()
    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    out  = nodes.new('ShaderNodeOutputMaterial')
    mat.node_tree.links.new(bsdf.outputs['BSDF'], out.inputs['Surface'])
    bsdf.inputs['Base Color'].default_value     = (*color, 1.0)
    bsdf.inputs['Roughness'].default_value      = roughness
    bsdf.inputs['Metallic'].default_value       = metallic
    if emit > 0:
        bsdf.inputs['Emission Color'].default_value  = (*color, 1.0)
        bsdf.inputs['Emission Strength'].default_value = emit
    return mat

# ════════════════════════════════════════════════════════════════════════════
# 3. ROOM SHELL  (5m × 5m × 3m corner lab)
# ════════════════════════════════════════════════════════════════════════════
mat_brick    = make_mat('Mat_DarkBrick',    (0.10, 0.10, 0.10), roughness=0.95)
mat_concrete = make_mat('Mat_DarkConcrete', (0.13, 0.13, 0.13), roughness=0.90)

# Floor
bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 0, 0))
floor = bpy.context.object
floor.name = 'RoomFloor'
floor.scale = (5, 5, 1)
floor.data.materials.append(mat_concrete)
assign(floor, col_env)

# Back wall (behind desk, faces -Y)
bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 2.5, 1.5))
back_wall = bpy.context.object
back_wall.name = 'WallBack'
back_wall.scale = (5, 1, 3)
back_wall.rotation_euler = (math.radians(90), 0, 0)
back_wall.data.materials.append(mat_brick)
assign(back_wall, col_env)

# Left wall (faces +X from inside)
bpy.ops.mesh.primitive_plane_add(size=1, location=(-2.5, 0, 1.5))
left_wall = bpy.context.object
left_wall.name = 'WallLeft'
left_wall.scale = (5, 1, 3)
left_wall.rotation_euler = (math.radians(90), 0, math.radians(90))
left_wall.data.materials.append(mat_brick)
assign(left_wall, col_env)

# Ceiling
bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 0, 3))
ceiling = bpy.context.object
ceiling.name = 'RoomCeiling'
ceiling.scale = (5, 5, 1)
ceiling.rotation_euler = (math.radians(180), 0, 0)
ceiling.data.materials.append(mat_concrete)
assign(ceiling, col_env)

print('Room shell built: floor, 2 walls, ceiling')

# ════════════════════════════════════════════════════════════════════════════
# 4. MAIN DESK  (dark walnut top + brushed aluminum legs)
# ════════════════════════════════════════════════════════════════════════════
mat_walnut = make_mat('Mat_DarkWalnut',      (0.10, 0.05, 0.02), roughness=0.85)
mat_alumin = make_mat('Mat_BrushedAluminum', (0.53, 0.53, 0.53), roughness=0.35, metallic=0.9)

# Desk top — heavy, wide: 2.0m wide × 0.9m deep × 0.05m thick
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 1.2, 0.775))
desk_top = bpy.context.object
desk_top.name = 'MainDesk'
desk_top.scale = (1.0, 0.45, 0.025)
desk_top.data.materials.append(mat_walnut)
assign(desk_top, col_desk)

# Four legs — tapered aluminum, 75cm tall
leg_positions = [(-0.85, 0.82, 0.375), (0.85, 0.82, 0.375),
                 (-0.85, 1.58, 0.375), (0.85, 1.58, 0.375)]
for i, pos in enumerate(leg_positions):
    bpy.ops.mesh.primitive_cube_add(size=1, location=pos)
    leg = bpy.context.object
    leg.name = f'DeskLeg_{i+1}'
    leg.scale = (0.03, 0.03, 0.375)
    leg.data.materials.append(mat_alumin)
    leg.parent = desk_top
    assign(leg, col_desk)

print('Desk built: top + 4 aluminum legs')

# ════════════════════════════════════════════════════════════════════════════
# 5. ARCHITECT'S DESK LAMP  (warm amber — primary light source)
# ════════════════════════════════════════════════════════════════════════════
mat_lamp_arm  = make_mat('Mat_LampArm',   (0.15, 0.15, 0.15), roughness=0.4, metallic=0.8)
mat_lamp_shade= make_mat('Mat_EmissiveAmber', (1.0, 0.67, 0.0), roughness=0.5, emit=3.0)

# Lamp base (on desk, left side)
bpy.ops.mesh.primitive_cylinder_add(radius=0.06, depth=0.02, location=(-0.6, 1.0, 0.81))
lamp_base = bpy.context.object; lamp_base.name = 'LampBase'
lamp_base.data.materials.append(mat_lamp_arm)
assign(lamp_base, col_desk)

# Lamp arm (vertical + horizontal segments)
bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=0.45, location=(-0.6, 1.0, 1.035))
lamp_v = bpy.context.object; lamp_v.name = 'LampArmV'
lamp_v.data.materials.append(mat_lamp_arm)
lamp_v.parent = lamp_base
assign(lamp_v, col_desk)

bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.35, location=(-0.425, 1.0, 1.26))
lamp_h = bpy.context.object; lamp_h.name = 'LampArmH'
lamp_h.rotation_euler = (0, math.radians(90), 0)
lamp_h.data.materials.append(mat_lamp_arm)
lamp_h.parent = lamp_base
assign(lamp_h, col_desk)

# Lamp shade (cone pointing down — emissive amber)
bpy.ops.mesh.primitive_cone_add(radius1=0.12, radius2=0.04, depth=0.15,
                                 location=(-0.25, 1.0, 1.19))
lamp_shade = bpy.context.object; lamp_shade.name = 'LampShade'
lamp_shade.rotation_euler = (math.radians(180), 0, 0)
lamp_shade.data.materials.append(mat_lamp_shade)
lamp_shade.parent = lamp_base
assign(lamp_shade, col_desk)

# Actual point light for the lamp
bpy.ops.object.light_add(type='POINT', location=(-0.25, 1.0, 1.1))
lamp_light = bpy.context.object; lamp_light.name = 'DeskLampLight'
lamp_light.data.color = (1.0, 0.67, 0.0)
lamp_light.data.energy = 80
lamp_light.data.shadow_soft_size = 0.15
assign(lamp_light, col_lighting)

print('Desk lamp built')

# ════════════════════════════════════════════════════════════════════════════
# 6. MONITOR  (cyan glow placeholder — back-right of desk)
# ════════════════════════════════════════════════════════════════════════════
mat_monitor_body  = make_mat('Mat_MattePlastic', (0.05, 0.05, 0.05), roughness=0.8)
mat_monitor_screen= make_mat('Mat_MonitorScreen', (0.0, 0.8, 0.6), roughness=0.1, emit=4.0)

bpy.ops.mesh.primitive_cube_add(size=1, location=(0.55, 1.55, 1.18))
mon_body = bpy.context.object; mon_body.name = 'MonitorBody'
mon_body.scale = (0.30, 0.025, 0.20)
mon_body.data.materials.append(mat_monitor_body)
assign(mon_body, col_desk)

bpy.ops.mesh.primitive_plane_add(size=1, location=(0.55, 1.525, 1.18))
mon_screen = bpy.context.object; mon_screen.name = 'MonitorScreen'
mon_screen.scale = (0.27, 1.0, 0.17)
mon_screen.rotation_euler = (math.radians(90), 0, 0)
mon_screen.data.materials.append(mat_monitor_screen)
mon_screen.parent = mon_body
assign(mon_screen, col_desk)

# Monitor stand
bpy.ops.mesh.primitive_cube_add(size=1, location=(0.55, 1.55, 0.83))
mon_stand = bpy.context.object; mon_stand.name = 'MonitorStand'
mon_stand.scale = (0.06, 0.06, 0.03)
mon_stand.data.materials.append(mat_monitor_body)
mon_stand.parent = mon_body
assign(mon_stand, col_desk)

# Cyan point light from monitor
bpy.ops.object.light_add(type='POINT', location=(0.55, 1.4, 1.18))
mon_light = bpy.context.object; mon_light.name = 'MonitorGlowLight'
mon_light.data.color = (0.0, 1.0, 0.8)
mon_light.data.energy = 30
assign(mon_light, col_lighting)

print('Monitor built')

# ════════════════════════════════════════════════════════════════════════════
# 7. REPOSITION CAMERA
# ════════════════════════════════════════════════════════════════════════════
cam = bpy.data.objects.get('SceneCamera')
if not cam:
    bpy.ops.object.camera_add()
    cam = bpy.context.object
    cam.name = 'SceneCamera'

cam.location = (-2.2, -1.5, 1.8)
cam.rotation_euler = (math.radians(75), 0, math.radians(-35))
bpy.context.scene.camera = cam
assign(cam, col_cameras)
print('Camera repositioned to face desk corner')

# ════════════════════════════════════════════════════════════════════════════
# 8. SAVE
# ════════════════════════════════════════════════════════════════════════════
bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
print('\nPhase 1 complete — Lab shell saved.')
print('   Objects in scene:', len(bpy.data.objects))
