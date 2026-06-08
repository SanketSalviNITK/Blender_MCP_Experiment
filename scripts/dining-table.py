# Reusable dining table builder using bmesh world-coordinate pattern
# Learned in Lesson 1.5 — always use this approach, never transform_apply
# Usage: run in Blender or via blender_cmd.py

import bpy, bmesh

def build_dining_table(
    width=3.0, depth=1.5, thickness=0.06,
    leg_height=0.72, leg_size=0.08, inset=0.12,
    color=(0.25, 0.12, 0.05), roughness=0.45
):
    """
    Build a dining table with 4 legs at exact world coordinates.
    All joints verified flush (gap < 0.001).

    Args:
        width      : table width in X (default 3.0m)
        depth      : table depth in Y (default 1.5m)
        thickness  : tabletop thickness (default 0.06m)
        leg_height : leg height / floor to table underside (default 0.72m)
        leg_size   : leg cross-section square side (default 0.08m)
        inset      : leg inset from table edge (default 0.12m)
        color      : RGB material colour tuple
        roughness  : material roughness 0–1
    """
    table_bottom = leg_height
    table_top    = leg_height + thickness
    leg_x        = width / 2 - inset
    leg_y        = depth / 2 - inset

    def walnut_mat(name):
        m = bpy.data.materials.new(name)
        m.use_nodes = True
        n = m.node_tree.nodes; n.clear()
        b = n.new('ShaderNodeBsdfPrincipled')
        b.inputs['Base Color'].default_value = (*color, 1.0)
        b.inputs['Roughness'].default_value = roughness
        o = n.new('ShaderNodeOutputMaterial')
        m.node_tree.links.new(b.outputs['BSDF'], o.inputs['Surface'])
        return m

    def make_box(name, x0, x1, y0, y1, z0, z1, mat):
        me = bpy.data.meshes.new(name + 'Mesh')
        bm = bmesh.new()
        v = [
            bm.verts.new((x0,y0,z0)), bm.verts.new((x1,y0,z0)),
            bm.verts.new((x1,y1,z0)), bm.verts.new((x0,y1,z0)),
            bm.verts.new((x0,y0,z1)), bm.verts.new((x1,y0,z1)),
            bm.verts.new((x1,y1,z1)), bm.verts.new((x0,y1,z1)),
        ]
        bm.faces.new([v[0],v[3],v[2],v[1]])
        bm.faces.new([v[4],v[5],v[6],v[7]])
        bm.faces.new([v[0],v[1],v[5],v[4]])
        bm.faces.new([v[2],v[3],v[7],v[6]])
        bm.faces.new([v[0],v[4],v[7],v[3]])
        bm.faces.new([v[1],v[2],v[6],v[5]])
        bm.to_mesh(me); bm.free(); me.update()
        obj = bpy.data.objects.new(name, me)
        bpy.context.scene.collection.objects.link(obj)
        obj.data.materials.append(mat)
        return obj

    # Build tabletop
    table = make_box('DiningTable',
        -width/2, width/2, -depth/2, depth/2,
        table_bottom, table_top, walnut_mat('WalnutTop'))

    # Build 4 legs
    corners = [
        ('TableLeg_1',  leg_x,  leg_y),
        ('TableLeg_2',  leg_x, -leg_y),
        ('TableLeg_3', -leg_x,  leg_y),
        ('TableLeg_4', -leg_x, -leg_y),
    ]
    for name, cx, cy in corners:
        make_box(name,
            cx-leg_size/2, cx+leg_size/2,
            cy-leg_size/2, cy+leg_size/2,
            0.0, leg_height, walnut_mat('WalnutLeg'))

    # Verify joints
    t_bot = min(v.co.z for v in table.data.vertices)
    all_ok = True
    for name, cx, cy in corners:
        leg = bpy.data.objects.get(name)
        leg_top = max(v.co.z for v in leg.data.vertices)
        ok = abs(t_bot - leg_top) < 0.001
        all_ok = all_ok and ok
        print(f'{name}: joint flush={ok}')
    print(f'Table surface Z: {table_bottom} to {table_top}')
    print(f'All joints flush: {all_ok}')
    return table


# Run directly
build_dining_table()
