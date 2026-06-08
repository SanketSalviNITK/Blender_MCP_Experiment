# PBR Materials for the Rustic Dining Table Scene
# Learned in Lesson 2.2
# Run after scene objects are built.

import bpy


def make_principled(name, color, roughness, metallic=0.0, transmission=0.0):
    """
    Create or replace a Principled BSDF material.

    Args:
        name         : material name (string)
        color        : (R, G, B) tuple in 0-1 range
        roughness    : 0 (mirror) to 1 (fully matte)
        metallic     : 0 (non-metal) to 1 (metal)
        transmission : 0 (opaque) to 1 (fully transparent glass)

    Returns:
        bpy.types.Material
    """
    mat = bpy.data.materials.get(name)
    if mat:
        mat.node_tree.nodes.clear()
    else:
        mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    out  = nodes.new('ShaderNodeOutputMaterial')
    links.new(bsdf.outputs['BSDF'], out.inputs['Surface'])

    bsdf.inputs['Base Color'].default_value = (color[0], color[1], color[2], 1.0)
    bsdf.inputs['Roughness'].default_value  = roughness
    bsdf.inputs['Metallic'].default_value   = metallic
    if transmission > 0:
        bsdf.inputs['Transmission Weight'].default_value = transmission
    return mat


def assign_material(obj_name, mat):
    """Assign a material to a mesh object, replacing all existing slots."""
    obj = bpy.data.objects.get(obj_name)
    if not obj or obj.type != 'MESH':
        print('SKIP (not mesh): {}'.format(obj_name))
        return
    obj.data.materials.clear()
    obj.data.materials.append(mat)
    print('OK: {} -> {}'.format(obj_name, mat.name))


def apply_scene_materials():
    # --- Wood ---
    walnut = make_principled('WalnutWood', (0.12, 0.06, 0.02), roughness=0.75)
    for n in ['DiningTable', 'TableLeg_1', 'TableLeg_2', 'TableLeg_3', 'TableLeg_4']:
        assign_material(n, walnut)

    # --- Ceramic ---
    ceramic = make_principled('WhiteCeramic', (0.92, 0.92, 0.92), roughness=0.15)
    for n in ['CoffeeMug', 'MugHandle']:
        assign_material(n, ceramic)

    # --- Book ---
    assign_material('RedBook', make_principled('RedBookCloth', (0.55, 0.05, 0.04), roughness=0.80))

    # --- Floor ---
    assign_material('Floor', make_principled('StoneConcrete', (0.35, 0.32, 0.28), roughness=0.85))

    # --- Wall ---
    assign_material('StoneWall', make_principled('AgedPlaster', (0.55, 0.50, 0.44), roughness=0.90))

    # --- Metal lamp ---
    steel = make_principled('BrushedSteel', (0.60, 0.60, 0.60), roughness=0.35, metallic=0.9)
    for n in ['LampBase', 'LampPole']:
        assign_material(n, steel)

    # --- Frosted glass globe ---
    assign_material('LampGlassSphere',
                    make_principled('FrostedGlass', (0.95, 0.92, 0.85),
                                    roughness=0.05, transmission=0.85))

    # --- Lamp glow (LIGHT object, set colour directly) ---
    lamp = bpy.data.objects.get('LampGlow')
    if lamp and lamp.type == 'LIGHT':
        lamp.data.color  = (1.0, 0.95, 0.8)
        lamp.data.energy = 60
        print('OK: LampGlow colour set to warm white (1.0, 0.95, 0.8), energy=60')

    print('Scene materials complete.')


apply_scene_materials()
