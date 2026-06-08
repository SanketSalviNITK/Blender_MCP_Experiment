# Parent a list of child objects to a parent object
# preserving their world transforms (no jumping on parent assignment)
# Learned in Lesson 2.1

import bpy

def parent_to(parent_name, child_names):
    """
    Parent a list of objects to a parent, preserving world positions.

    Args:
        parent_name : name of the parent object (string)
        child_names : list of child object names

    Example:
        parent_to('DiningTable', ['TableLeg_1','TableLeg_2','TableLeg_3','TableLeg_4'])
    """
    parent = bpy.data.objects.get(parent_name)
    if not parent:
        print('Parent not found: {}'.format(parent_name))
        return

    for name in child_names:
        child = bpy.data.objects.get(name)
        if not child:
            print('Child not found: {}'.format(name))
            continue
        world_mat = child.matrix_world.copy()
        child.parent = parent
        child.matrix_world = world_mat
        print('{} -> parent = {}'.format(name, parent_name))

    bpy.context.view_layer.update()
    print('Done. Transform {} to move all children together.'.format(parent_name))


# Example usage:
parent_to('DiningTable', ['TableLeg_1', 'TableLeg_2', 'TableLeg_3', 'TableLeg_4'])
