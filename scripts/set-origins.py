# Set origin to geometry centre for all mesh objects in scene
# Learned in Lesson 2.1
# Usage: run via blender_cmd.py or in Blender Script Editor

import bpy, bmesh
from mathutils import Vector

def set_origin_to_geometry_center(obj):
    """
    Set object origin to bounding box centre.
    Moves mesh vertices in local space and updates object.location.
    Works reliably via TCP bridge (no bpy.ops dependency).
    """
    world_verts = [(obj.matrix_world @ v.co) for v in obj.data.vertices]
    cx = (max(v.x for v in world_verts) + min(v.x for v in world_verts)) / 2
    cy = (max(v.y for v in world_verts) + min(v.y for v in world_verts)) / 2
    cz = (max(v.z for v in world_verts) + min(v.z for v in world_verts)) / 2
    centre = Vector((cx, cy, cz))

    bm = bmesh.new()
    bm.from_mesh(obj.data)
    offset = obj.matrix_world.inverted() @ centre
    for v in bm.verts:
        v.co -= offset
    bm.to_mesh(obj.data)
    bm.free()
    obj.data.update()
    obj.location = centre
    return centre


def set_all_origins():
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            c = set_origin_to_geometry_center(obj)
            print('{}: origin -> ({}, {}, {})'.format(
                obj.name, round(c.x,3), round(c.y,3), round(c.z,3)))


set_all_origins()
