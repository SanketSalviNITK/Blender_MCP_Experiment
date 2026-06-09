import bpy

# ─── Helper: parent B to A without moving B in world space ───────────────────
def set_parent(child, parent):
    if child.parent == parent:
        return
    # Unparent first
    if child.parent:
        mw = child.matrix_world.copy()
        child.parent = None
        child.matrix_world = mw
        bpy.context.view_layer.update()
    mw_final = child.matrix_world.copy()
    child.parent = parent
    child.matrix_world = mw_final
    bpy.context.view_layer.update()
    print(f"  Parented '{child.name}' -> '{parent.name}'")

# ─── Helper: move object to a collection (remove from all others first) ──────
def move_to_collection(obj, col):
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    col.objects.link(obj)

# ─── Helper: get or create a top-level collection ────────────────────────────
def get_or_create(name, parent_col=None):
    if name in bpy.data.collections:
        col = bpy.data.collections[name]
    else:
        col = bpy.data.collections.new(name)
        print(f"  Created collection '{name}'")
    target = parent_col if parent_col else bpy.context.scene.collection
    if col.name not in [c.name for c in target.children]:
        target.children.link(col)
    return col

# ════════════════════════════════════════════════════════════════════════════
# 1. CREATE TARGET COLLECTIONS
# ════════════════════════════════════════════════════════════════════════════
print("\n=== Creating collections ===")
col_furniture   = get_or_create("Furniture")
col_plant       = get_or_create("DecorativePlant")
col_tableitems  = get_or_create("TableItems")
col_bookshelf   = get_or_create("Bookshelf")
col_books       = get_or_create("Books", col_bookshelf)   # nested under Bookshelf
col_shelf_deco  = get_or_create("ShelfDecorations", col_bookshelf)
col_lamp        = get_or_create("Lamp")
col_lighting    = get_or_create("Lighting")
col_environment = get_or_create("Environment")
col_cameras     = get_or_create("Cameras")

# ════════════════════════════════════════════════════════════════════════════
# 2. FIX PARENT-CHILD RELATIONSHIPS
# ════════════════════════════════════════════════════════════════════════════
print("\n=== Fixing parent-child relationships ===")
o = bpy.data.objects

# SideTable legs → SideTable
side_table = o['SideTable']
for leg in ['SideTableLeg_1', 'SideTableLeg_2', 'SideTableLeg_3', 'SideTableLeg_4']:
    set_parent(o[leg], side_table)

# MugHandle → CoffeeMug (same decorative unit)
set_parent(o['MugHandle'], o['CoffeeMug'])

# Lamp parts → LampBase (one lamp assembly)
for part in ['LampPole', 'LampGlassSphere', 'DustMotes']:
    set_parent(o[part], o['LampBase'])

# ════════════════════════════════════════════════════════════════════════════
# 3. ASSIGN OBJECTS TO COLLECTIONS
# ════════════════════════════════════════════════════════════════════════════
print("\n=== Assigning to collections ===")

# --- Furniture (roots only — legs follow via parent) ---
for name in ['DiningTable', 'TableLeg_1', 'TableLeg_2', 'TableLeg_3', 'TableLeg_4',
             'SideTable', 'SideTableLeg_1', 'SideTableLeg_2', 'SideTableLeg_3', 'SideTableLeg_4']:
    move_to_collection(o[name], col_furniture)

# --- DecorativePlant (pot + plant as one unit) ---
for name in ['PlantPot', 'AloeVera']:
    move_to_collection(o[name], col_plant)

# --- TableItems ---
for name in ['CoffeeMug', 'MugHandle', 'GlassesCase', 'LinenNapkin', 'LoosePaper', 'RedBook']:
    move_to_collection(o[name], col_tableitems)

# --- Bookshelf structure (root + all structural children) ---
shelf_structure = [
    'Shelf_Left', 'Shelf_Right', 'Shelf_1', 'Shelf_2', 'Shelf_3', 'Shelf_4',
    'Shelf_Back', 'Shelf_Bottom', 'Shelf_Top'
]
for name in shelf_structure:
    move_to_collection(o[name], col_bookshelf)

# --- Books (separate assets — individual books) ---
book_names = [f'Book_S{s}_{n}' for s in range(1, 4) for n in range(1, 7)
              if f'Book_S{s}_{n}' in o]
book_names += ['FloorBook_1', 'FloorBook_2']
# Keep books parented to shelf (they're positionally tied), just re-collect
for name in book_names:
    if name in o:
        move_to_collection(o[name], col_books)

# --- ShelfDecorations ---
move_to_collection(o['Candle'], col_shelf_deco)

# --- Lamp assembly ---
for name in ['LampBase', 'LampPole', 'LampGlassSphere', 'DustMotes']:
    move_to_collection(o[name], col_lamp)

# --- Lighting ---
for name in ['FillLight', 'LampGlow', 'RimLight', 'WindowLight']:
    move_to_collection(o[name], col_lighting)

# --- Environment ---
for name in ['Floor', 'StoneWall']:
    move_to_collection(o[name], col_environment)

# --- Cameras ---
move_to_collection(o['SceneCamera'], col_cameras)

# ════════════════════════════════════════════════════════════════════════════
# 4. CLEAN UP OLD EMPTY COLLECTIONS
# ════════════════════════════════════════════════════════════════════════════
print("\n=== Removing old empty collections ===")
old_names = ['DiningSet']  # previously used; now empty
for name in old_names:
    if name in bpy.data.collections:
        col = bpy.data.collections[name]
        if len(col.objects) == 0 and len(col.children) == 0:
            # Unlink from scene before removing
            for parent_col in bpy.data.collections:
                if col.name in [c.name for c in parent_col.children]:
                    parent_col.children.unlink(col)
            if col.name in [c.name for c in bpy.context.scene.collection.children]:
                bpy.context.scene.collection.children.unlink(col)
            bpy.data.collections.remove(col)
            print(f"  Removed empty collection '{name}'")
        else:
            print(f"  Skipped '{name}' (still has {len(col.objects)} objects)")

# ════════════════════════════════════════════════════════════════════════════
# 5. SUMMARY REPORT
# ════════════════════════════════════════════════════════════════════════════
print("\n=== Final collection layout ===")
def print_col(col, indent=0):
    obj_names = [o.name for o in col.objects]
    print(f"{'  '*indent}[{col.name}]  ({len(obj_names)} objects)")
    for name in sorted(obj_names):
        print(f"{'  '*indent}  - {name}")
    for child in col.children:
        print_col(child, indent + 1)

print_col(bpy.context.scene.collection)

# Save
bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
print("\nScene saved.")
