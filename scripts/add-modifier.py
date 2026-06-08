# Reusable modifier helper for Blender objects
# Learned in Lesson 1.4

import bpy

def add_modifier(obj_name, mod_type, mod_name=None, **settings):
    """
    Add a modifier to a named object with optional settings.

    Args:
        obj_name: Name of the object (string)
        mod_type: Modifier type ID e.g. 'SUBSURF', 'ARRAY', 'MIRROR'
        mod_name: Optional name for the modifier
        **settings: Any modifier properties as keyword args

    Returns:
        The modifier object, or None if object not found

    Examples:
        add_modifier('RedCube', 'SUBSURF', levels=2, render_levels=2)
        add_modifier('MySphere', 'ARRAY', count=5)
        add_modifier('MyMesh', 'MIRROR', use_axis=(True, False, False))
        add_modifier('MyMesh', 'BEVEL', width=0.1, segments=3)
    """
    obj = bpy.data.objects.get(obj_name)
    if not obj:
        print(f"Object '{obj_name}' not found in scene.")
        return None

    name = mod_name or mod_type.capitalize()
    mod = obj.modifiers.new(name=name, type=mod_type)

    for key, value in settings.items():
        if hasattr(mod, key):
            setattr(mod, key, value)
        else:
            print(f"Warning: modifier has no property '{key}'")

    print(f"Modifier '{mod.name}' ({mod_type}) added to '{obj_name}'")
    return mod


# --- Common Modifier Presets ---

def add_subsurf(obj_name, levels=2):
    return add_modifier(obj_name, 'SUBSURF', 'Subdivision',
                        levels=levels,
                        render_levels=levels,
                        subdivision_type='CATMULL_CLARK')

def add_array(obj_name, count=3, offset_x=2.0):
    mod = add_modifier(obj_name, 'ARRAY', 'Array', count=count)
    if mod:
        mod.relative_offset_displace[0] = offset_x
    return mod

def add_mirror(obj_name, axis='X'):
    mod = add_modifier(obj_name, 'MIRROR', f'Mirror_{axis}')
    if mod:
        mod.use_axis[0] = (axis == 'X')
        mod.use_axis[1] = (axis == 'Y')
        mod.use_axis[2] = (axis == 'Z')
    return mod

def add_bevel(obj_name, width=0.1, segments=2):
    return add_modifier(obj_name, 'BEVEL', 'Bevel',
                        width=width,
                        segments=segments)


# --- Usage Examples ---
# add_subsurf('RedCube', levels=2)
# add_array('RedCube', count=4, offset_x=2.5)
# add_mirror('RedCube', axis='X')
# add_bevel('RedCube', width=0.05, segments=3)
