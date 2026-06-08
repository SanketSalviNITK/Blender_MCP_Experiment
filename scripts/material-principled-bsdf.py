# Reusable Principled BSDF material creator
# Usage: call create_material(obj, name, color, roughness, metallic)
# Learned in Lesson 1.3

import bpy

def create_material(obj, name, color=(1,1,1), roughness=0.4, metallic=0.0):
    """
    Create and assign a Principled BSDF material to an object.

    Args:
        obj: Blender object to assign material to
        name: Material name (string)
        color: RGB tuple e.g. (1.0, 0.0, 0.0) for red
        roughness: 0.0 = glossy, 1.0 = fully matte
        metallic: 0.0 = non-metal, 1.0 = fully metallic
    """
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    nodes.clear()

    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    bsdf.location = (0, 0)
    bsdf.inputs['Base Color'].default_value = (*color, 1.0)
    bsdf.inputs['Roughness'].default_value = roughness
    bsdf.inputs['Metallic'].default_value = metallic

    output = nodes.new('ShaderNodeOutputMaterial')
    output.location = (300, 0)
    mat.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])

    obj.data.materials.clear()
    obj.data.materials.append(mat)
    return mat


# Example usage:
# cube = bpy.data.objects['RedCube']
# create_material(cube, 'RedMaterial', color=(1.0, 0.0, 0.0), roughness=0.4)
