# Reusable coffee mug builder — hollow cylinder + upright torus handle
# Learned in Lesson 1.5
# Usage: run in Blender or via blender_cmd.py

import bpy, bmesh, math

def build_coffee_mug(
    x=0.0, y=0.0, base_z=0.0,
    outer_r=0.045, inner_r=0.038, height=0.09,
    handle_major_r=0.028, handle_minor_r=0.007,
    color=(0.96, 0.95, 0.93), roughness=0.12,
    segs=32
):
    """
    Build a hollow ceramic coffee mug with upright torus handle.

    Args:
        x, y       : XY centre position
        base_z     : Z of mug bottom (set to table top surface)
        outer_r    : outer radius of mug body
        inner_r    : inner radius (wall = outer_r - inner_r)
        height     : mug height
        handle_major_r : handle loop radius
        handle_minor_r : handle tube thickness
        color      : RGB colour tuple
        roughness  : material roughness
        segs       : cylinder smoothness segments
    """
    top_z  = base_z + height
    cen_z  = base_z + height / 2

    def ceramic_mat(name):
        m = bpy.data.materials.new(name)
        m.use_nodes = True
        n = m.node_tree.nodes; n.clear()
        b = n.new('ShaderNodeBsdfPrincipled')
        b.inputs['Base Color'].default_value = (*color, 1.0)
        b.inputs['Roughness'].default_value = roughness
        b.inputs['Specular IOR Level'].default_value = 0.9
        o = n.new('ShaderNodeOutputMaterial')
        m.node_tree.links.new(b.outputs['BSDF'], o.inputs['Surface'])
        return m

    mat = ceramic_mat('CeramicWhite')

    # ── MUG BODY (hollow cylinder) ────────────────────────────
    me = bpy.data.meshes.new('CoffeeMugMesh')
    bm = bmesh.new()
    ob, ot, ib, it_ = [], [], [], []
    for i in range(segs):
        a = 2 * math.pi * i / segs
        c, s = math.cos(a), math.sin(a)
        ob.append(bm.verts.new((x + outer_r*c, y + outer_r*s, base_z)))
        ot.append(bm.verts.new((x + outer_r*c, y + outer_r*s, top_z)))
        ib.append(bm.verts.new((x + inner_r*c, y + inner_r*s, base_z + 0.005)))
        it_.append(bm.verts.new((x + inner_r*c, y + inner_r*s, top_z)))
    for i in range(segs):
        j = (i+1) % segs
        bm.faces.new([ob[i], ob[j], ot[j], ot[i]])       # outer wall
        bm.faces.new([ib[i], it_[i], it_[j], ib[j]])     # inner wall
        bm.faces.new([ob[i], ib[i], ib[j], ob[j]])       # bottom ring
        bm.faces.new([ot[i], ot[j], it_[j], it_[i]])     # top rim
    bm.to_mesh(me); bm.free(); me.update()
    mug = bpy.data.objects.new('CoffeeMug', me)
    bpy.context.scene.collection.objects.link(mug)
    mug.data.materials.append(mat)

    # ── HANDLE (upright torus on +X side) ─────────────────────
    hx     = x + outer_r + handle_major_r
    ms     = 20    # major segments
    ts     = 10    # minor (tube) segments
    me2    = bpy.data.meshes.new('MugHandleMesh')
    bm2    = bmesh.new()
    rings  = []
    for i in range(ms):
        a_maj = 2 * math.pi * i / ms
        rx    = hx + handle_major_r * math.cos(a_maj)
        rz    = cen_z + handle_major_r * math.sin(a_maj)
        ring  = []
        for j in range(ts):
            a_min = 2 * math.pi * j / ts
            nx, nz = math.cos(a_maj), math.sin(a_maj)
            bx = rx + handle_minor_r * math.cos(a_min) * nx
            by = y  + handle_minor_r * math.sin(a_min)
            bz = rz + handle_minor_r * math.cos(a_min) * nz
            ring.append(bm2.verts.new((bx, by, bz)))
        rings.append(ring)
    for i in range(ms):
        ni = (i+1) % ms
        for j in range(ts):
            nj = (j+1) % ts
            bm2.faces.new([rings[i][j], rings[ni][j], rings[ni][nj], rings[i][nj]])
    bm2.to_mesh(me2); bm2.free(); me2.update()
    handle = bpy.data.objects.new('MugHandle', me2)
    bpy.context.scene.collection.objects.link(handle)
    handle.data.materials.append(mat)

    print(f'Coffee mug built at ({x}, {y}), base Z={base_z}')
    print(f'  Body: outer_r={outer_r}, inner_r={inner_r}, height={height}')
    print(f'  Handle: major_r={handle_major_r}, minor_r={handle_minor_r}, upright XZ plane')
    return mug, handle


# Run directly — place on a table at Z=0.78
build_coffee_mug(x=-1.2, y=0.05, base_z=0.78)
