# Scene Collections — organise all objects into named groups
# Learned in Lesson 2.4
# Run after all scene objects exist.

import bpy


def get_or_create_collection(name):
    """Get existing collection or create and link to scene root."""
    col = bpy.data.collections.get(name)
    if not col:
        col = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(col)
    return col


def move_to_collection(obj_name, col):
    """Move object to target collection, removing it from all others."""
    obj = bpy.data.objects.get(obj_name)
    if not obj:
        print('NOT FOUND: {}'.format(obj_name))
        return
    # Unlink from every collection currently holding it
    for c in bpy.data.collections:
        if obj.name in c.objects:
            c.objects.unlink(obj)
    root = bpy.context.scene.collection
    if obj.name in root.objects:
        root.objects.unlink(obj)
    col.objects.link(obj)


def setup_collections():
    """
    Organise the dining table scene into 5 named collections:

    Scene Collection
    ├── Environment  — Floor, StoneWall
    ├── DiningSet    — Table, Legs, Book, Mug, Handle
    ├── Lamp         — LampPole, LampBase, LampGlassSphere, DustMotes
    ├── Lighting     — WindowLight, FillLight, RimLight, LampGlow
    └── Cameras      — SceneCamera
    """
    env     = get_or_create_collection('Environment')
    dining  = get_or_create_collection('DiningSet')
    lamp    = get_or_create_collection('Lamp')
    lights  = get_or_create_collection('Lighting')
    cameras = get_or_create_collection('Cameras')

    for n in ['Floor', 'StoneWall']:
        move_to_collection(n, env)

    for n in ['DiningTable', 'TableLeg_1', 'TableLeg_2', 'TableLeg_3', 'TableLeg_4',
              'RedBook', 'CoffeeMug', 'MugHandle']:
        move_to_collection(n, dining)

    for n in ['LampPole', 'LampBase', 'LampGlassSphere', 'DustMotes']:
        move_to_collection(n, lamp)

    for n in ['WindowLight', 'FillLight', 'RimLight', 'LampGlow']:
        move_to_collection(n, lights)

    move_to_collection('SceneCamera', cameras)

    # Remove the empty default startup collection if present
    default = bpy.data.collections.get('Collection')
    if default and len(default.objects) == 0 and len(default.children) == 0:
        bpy.context.scene.collection.children.unlink(default)
        bpy.data.collections.remove(default)

    bpy.context.view_layer.update()

    # Report
    print('=== COLLECTIONS ===')
    for col in bpy.data.collections:
        names = [o.name for o in col.objects]
        print('  [{}] ({}) {}'.format(col.name, len(names), names))

    root_objs = list(bpy.context.scene.collection.objects)
    if root_objs:
        print('WARNING orphan objects at root:', [o.name for o in root_objs])
    else:
        print('Root clean.')


setup_collections()
