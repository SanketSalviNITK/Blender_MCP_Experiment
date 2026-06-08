# Three-point lighting rig + camera setup for the Rustic Dining Table Scene
# Learned in Lesson 2.3
# Run after scene objects and materials are set up.

import bpy, math
from mathutils import Vector


def setup_lights():
    """
    Three-point lighting rig:
      - WindowLight (KEY)  — warm golden area light from upper-left
      - FillLight          — cool blue-grey area light from right (soft bounce)
      - RimLight           — warm area backlight, separates table from wall
      - LampGlow           — practical table lamp (POINT, already in scene)
    """

    # --- KEY: WindowLight (already exists, upgrade it) ---
    win = bpy.data.objects.get('WindowLight')
    if win:
        win.location = (-6.0, -1.0, 4.5)
        win.rotation_euler = (math.radians(55), 0, math.radians(-35))
        win.data.energy = 600
        win.data.color  = (1.0, 0.88, 0.65)   # warm golden afternoon
        win.data.size   = 3.0
        print('WindowLight (KEY): energy=600, warm golden, 3m area')

    # --- FILL: add if missing ---
    fill_obj = bpy.data.objects.get('FillLight')
    if not fill_obj:
        fill = bpy.data.lights.new(name='FillLight', type='AREA')
        fill_obj = bpy.data.objects.new('FillLight', fill)
        bpy.context.scene.collection.objects.link(fill_obj)

    fill_obj.location = (5.0, 2.0, 3.0)
    fill_obj.rotation_euler = (math.radians(45), 0, math.radians(130))
    fill_obj.data.energy = 80
    fill_obj.data.color  = (0.72, 0.82, 1.0)  # cool blue-grey, ambient bounce
    fill_obj.data.size   = 2.5
    print('FillLight (FILL): energy=80, cool blue, 2.5m area')

    # --- RIM: add if missing ---
    rim_obj = bpy.data.objects.get('RimLight')
    if not rim_obj:
        rim = bpy.data.lights.new(name='RimLight', type='AREA')
        rim_obj = bpy.data.objects.new('RimLight', rim)
        bpy.context.scene.collection.objects.link(rim_obj)

    rim_obj.location = (0.0, 5.5, 5.0)
    rim_obj.rotation_euler = (math.radians(130), 0, 0)
    rim_obj.data.energy = 150
    rim_obj.data.color  = (1.0, 0.92, 0.75)   # warm backlight
    rim_obj.data.size   = 2.0
    print('RimLight (RIM): energy=150, warm, 2m area')

    # --- PRACTICAL: LampGlow table lamp ---
    lamp = bpy.data.objects.get('LampGlow')
    if lamp and lamp.type == 'LIGHT':
        lamp.data.energy = 80
        lamp.data.color  = (1.0, 0.95, 0.8)
        print('LampGlow (PRACTICAL): energy=80, warm white point')


def setup_camera():
    """
    85mm portrait lens, f/1.8 DOF focused on CoffeeMug.
    Position: (5, -5.8, 2.4) — slightly elevated, 3/4 front angle.
    """
    cam_obj = bpy.data.objects.get('SceneCamera')
    mug_obj = bpy.data.objects.get('CoffeeMug')

    if not cam_obj:
        print('SceneCamera not found')
        return

    cam_obj.location       = (5.0, -5.8, 2.4)
    cam_obj.rotation_euler = (math.radians(78), 0, math.radians(43))
    cam_obj.data.lens      = 85.0

    # DOF focused on mug
    if mug_obj:
        dist = (cam_obj.location - mug_obj.location).length
        cam_obj.data.dof.use_dof        = True
        cam_obj.data.dof.aperture_fstop = 1.8
        cam_obj.data.dof.focus_distance = dist
        print('Camera: 85mm, f/1.8, focus={:.2f}m to mug'.format(dist))


def print_rig_summary():
    print()
    print('=== LIGHTING RIG ===')
    for obj in sorted(bpy.data.objects, key=lambda o: o.name):
        if obj.type == 'LIGHT':
            l = obj.data
            print('  {:<18} {:<6} energy={:<6} color=({:.2f},{:.2f},{:.2f})'.format(
                obj.name, l.type, round(l.energy, 0),
                l.color[0], l.color[1], l.color[2]))
    cam = bpy.data.objects.get('SceneCamera')
    if cam:
        c = cam.data
        print()
        print('=== CAMERA ===')
        print('  lens={}mm  f/{}'.format(c.lens, c.dof.aperture_fstop))
        print('  focus_distance={:.2f}m'.format(c.dof.focus_distance))
        print('  location=({:.2f},{:.2f},{:.2f})'.format(*cam.location))


setup_lights()
setup_camera()
print_rig_summary()
