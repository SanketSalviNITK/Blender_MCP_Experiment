# Scene Blueprint — The Missing Scientist's Lab
> Master reference document. Derived from: spec files, reference image, and 10s intro video.
> Last updated: 2026-06-09

---

## 0. The Story in One Sentence
*Dr. Sanket Salvi — Spatial Computing & IoT researcher — has just vanished into the digital realm.
His chair is empty. His coffee is still warm. His hologram projector is still on.*

---

## 1. Technical Contract (WebGL Export)

| Property | Value |
|----------|-------|
| Final format | `.glb` (glTF Binary) |
| Target engine | React Three Fiber (WebGL) |
| Max triangles | 100,000 |
| Max texture size | 4K atlas (2K preferred) |
| Max file size | 10 MB |
| Lighting method | Fully baked — no real-time lights in export |
| Detail method | Normal maps, NOT high-poly geometry |
| Target framerate | 60 fps in browser |

---

## 2. Room Layout (Confirmed from Video)

```
         BACK WALL (certificates + papers on plaster/stone)
    ┌─────────────────────────────────────────────────┐
    │  [Cert] [Cert] [Cert]  │  DESK (oak, right      │
    │  [Cert]  papers pinned │  corner area)           │
L   │                        │  lamp / laptop /        │  R
E   │                        │  hologram               │  I
F   │                        │                         │  G
T   ├───────────────────────────────────────────────── │  H
    │  BOOKSHELF L │ BOOKSHELF R  (entire left wall)   │  T
W   │  floor-to-ceiling, dense books                  │
A   │                                                  │  W
L   │                        DESK CHAIR (empty,        │  A
L   │                        jacket draped over back)  │  L
    │                                                  │  L
    └──────────────[DOOR]─────────────────────────────  │
         FRONT WALL                              [WINDOW]
                                          rain / city / curtain
```

### Exact Dimensions
- Room: **5m wide × 5m deep × 3m tall**
- Door: front-left wall, ~0.9m wide × 2.1m tall
- Window: right wall, ~1.8m wide × 2.2m tall, starts at ~0.5m from floor
- Desk: pushed into back-right corner, ~1.6m wide × 0.8m deep

---

## 3. Camera — Final Position (Video Frame 9.9s)

This is the exact frame where the video ends and the 3D scene begins.

| Property | Value |
|----------|-------|
| Position | Inside room, slightly left of centre |
| Location (approx) | (-1.5, -1.0, 1.6) |
| Looking toward | Back-right corner (desk + window simultaneously) |
| Height | ~1.6m — standing eye level |
| Focal length | 28–35mm (wide — captures bookshelf L + desk C + window R) |
| What's in frame | Bookshelf (left 30%), Desk + hologram (centre 40%), Window + rain (right 30%) |

### Camera Journey (for R3F animation reference)
1. **0:00** — Dark hallway, looking through open door at the lab
2. **2.5s** — Push through doorway into room
3. **5.0s** — Move forward/right, desk + hologram come into view
4. **7.5s** — Sweep right — window + rain dramatically revealed
5. **9.9s** — Settle into final position → **3D scene takes over here**

---

## 4. Lighting

### Mood
**Deep cold blue dominates.** The rainy city outside is the primary light source —
a strong cool ambient wash from the right window. The desk lamp is warm amber
but secondary — it creates a small pool on the desk only, mostly overwhelmed by the blue.

| Light Name | Type | Colour | Energy | Position | Purpose |
|------------|------|--------|--------|----------|---------|
| `WindowAmbient` | Area | Cold blue `#4A6FA5` | 40W | Right wall, window position | Dominant — rainy city glow |
| `DeskLampLight` | Point | Warm amber `#FFAA00` | 60W | Above lamp shade (-0.5, 0.8, 1.1) | Small warm pool on desk |
| `HologramGlow` | Point | Teal `#00FFCC` | 20W | Above desk centre (0.2, 0.8, 1.2) | Hologram uplight |
| `AmbientFill` | Point | Dark blue `#0A0F1A` | 5W | Room centre | Prevent pure black in corners |
| World | — | Black `#000000` | 0.0 | — | No ambient |

### LampShade Material
- Emissive amber `(1.0, 0.67, 0.0)`, strength 2.5
- Cone pointing **downward**

### HologramProjector Lens Material
- Emissive teal `(0.0, 1.0, 0.8)`, strength 5.0

---

## 5. Object Manifest

### 5A. Room Shell

| Blender Name | Description | Dimensions | Material |
|--------------|-------------|------------|---------|
| `RoomFloor` | Warm wooden parquet planks | 5×5m | `Mat_WoodFloor` — warm oak `#8B6914` roughness 0.8 |
| `WallBack` | Plaster/stone — certificates hang here | 5×3m | `Mat_Plaster` — off-white `#D4C9A8` roughness 0.95 |
| `WallLeft` | Left wall — bookshelf against it | 5×3m | `Mat_Plaster` same |
| `WallRight` | Right wall — window cut out | 5×3m | `Mat_Plaster` same |
| `WallFront` | Front wall — door cut out | 5×3m | `Mat_Plaster` same |
| `RoomCeiling` | Flat ceiling | 5×5m | `Mat_Ceiling` — light grey `#CCCCCC` roughness 1.0 |
| `DoorFrame` | Door opening, front-left | 0.9×2.1m | `Mat_DarkWood` |
| `WindowFrame` | Window opening, right wall | 1.8×2.2m | `Mat_WhitePaint` — white `#EEEEEE` roughness 0.5 |
| `WindowGlass` | Glass pane — rain streaks texture | 1.75×2.15m | `Mat_RainyGlass` — dark blue tint, alpha 0.15 |
| `RainCurtain` | Fabric curtain, blowing inward | 0.8×2.2m | `Mat_Curtain` — blue-grey fabric `#6B7FA3` roughness 0.9 |
| `CityBackdrop` | Plane outside window — city at night | 3×2.5m | `Mat_CityNight` — emissive city image/gradient |

### 5B. Bookshelf (Left Wall)

| Blender Name | Description |
|--------------|-------------|
| `Bookshelf_L` | Left bookshelf unit — 5 shelves, dark wood |
| `Bookshelf_R` | Right bookshelf unit — 5 shelves, dark wood |
| `Books_S*_*` | Individual books — varied spine colours |
| `Binder_*` | Ring binders — dark grey/black |
| `Trophy_01` | Glass award trophy |
| `Trophy_02` | Medallion/plaque |
| `ShelfPapers` | Stacked loose papers on shelves |

### 5C. Desk Assembly

| Blender Name | Description | Poly Budget |
|--------------|-------------|-------------|
| `MainDesk` | Medium oak/brown wood top, 1.6×0.8×0.05m | 500 |
| `DeskLeg_1..4` | Wooden legs (NOT aluminium — matches reference) | 400 |
| `DeskChair` | Wooden/leather office chair, tucked in | 1,500 |
| `ScientistJacket` | Dark jacket draped over chair back | 800 |
| `DeskLampBase` | Silver architect lamp base | 200 |
| `DeskLampArmV` | Vertical arm | 150 |
| `DeskLampArmH` | Horizontal arm | 150 |
| `DeskLampShade` | Cone shade, points down | 300 |
| `WireCluster_*` | 5× bezier wires draping off back edge | 400 |

### 5D. Desk Surface Items (Left to Right)

| Blender Name | Description | Position on Desk |
|--------------|-------------|-----------------|
| `SpeakerSmall` | Small compact speaker | Far left |
| `CoffeeMug` | White ceramic mug, half drunk | Left-centre |
| `PencilHolder` | Cup full of pens/pencils | Left-centre |
| `Notebook` | Open notebook, scribbled notes | Centre-left |
| `LoosePapers` | Scattered A4 sheets | Centre |
| `Laptop` | Open laptop, code on screen | Centre |
| `Mouse` | Computer mouse | Right of laptop |
| `HologramProjector` | ⭐ SACRED — retro hardware, teal lens | Centre-right |
| `IoTSensor` | Small white cube device | Far right |
| `SolderingIron` | Soldering iron, slightly smoking | Far right |
| `Headphones` | Over-ear headphones lying flat | Back-left |

### 5E. The 5 Sacred Meshes (NOT merged — R3F targets)

| Blender Name | R3F use | Description |
|--------------|---------|-------------|
| `HologramProjector` | Hologram trigger | Retro hardware — teal emissive lens pointing up |
| `HologramMolecule` | Animated hologram | Floating molecular network, teal/blue nodes+bonds |
| `RailwayDrone` | Project overlay | Miniature drone on cracked steel track segment |
| `HoloLens` | Project overlay | Partially disassembled AR headset |
| `RoboticArm` | Project overlay | Small teleoperated arm with glowing sensor |

### 5F. Back Wall — Certificates & Papers

| Blender Name | Description |
|--------------|-------------|
| `CertFrame_01..08` | Framed diplomas/certificates — gold frames, varied sizes |
| `WallPaper_01..06` | Loose A4 papers pinned directly to wall |
| `StickyNote_01..04` | Yellow sticky notes |
| `ShelfAboveDesk` | Narrow shelf above the certificates, books on top |

---

## 6. Material Palette

| Material Name | Base Colour | Roughness | Notes |
|---------------|-------------|-----------|-------|
| `Mat_WoodFloor` | `#8B6914` warm oak | 0.80 | Parquet planks |
| `Mat_Plaster` | `#D4C9A8` off-white | 0.95 | All walls |
| `Mat_DeskOak` | `#7B4F2E` medium brown | 0.82 | Desk surface |
| `Mat_DeskWood` | `#5C3A1E` darker brown | 0.85 | Desk legs/chair frame |
| `Mat_BookshelfWood` | `#3D2B1F` dark brown | 0.88 | Shelf units |
| `Mat_Paper` | `#D4C9A8` | 0.95 | Papers, certificates |
| `Mat_Leather` | `#1A1008` near-black | 0.70 | Chair seat |
| `Mat_Jacket` | `#0D0D0D` black | 0.85 | Scientist's jacket |
| `Mat_EmissiveTeal` | `#00FFCC` emit | — | Hologram glow, strength 5.0 |
| `Mat_EmissiveAmber` | `#FFAA00` emit | — | Lamp shade, strength 2.5 |
| `Mat_LaptopScreen` | `#001A33` emit | — | Blue-black code screen, strength 3.0 |
| `Mat_RainyGlass` | Dark blue tint | 0.05 | Window glass — alpha 0.15 |
| `Mat_Curtain` | `#6B7FA3` blue-grey | 0.90 | Fabric curtain |
| `Mat_CityNight` | Emissive city gradient | — | Outside backdrop, strength 1.5 |
| `Mat_Silver` | `#AAAAAA` | 0.30 | Lamp arms, metallic 0.8 |
| `Mat_WhiteCeramic` | `#EEEEEE` | 0.60 | Coffee mug |

---

## 7. Collection Structure

```
Scene Collection
├── Environment        — Room shell (walls, floor, ceiling, door, window, city backdrop)
├── Bookshelf          — Both shelf units + all books + binders + trophies
├── Desk               — Desk top, legs, lamp assembly, chair, jacket, wire clusters
├── DeskItems          — Everything sitting ON the desk surface
├── BackWall           — Certificate frames, pinned papers, sticky notes, shelf above desk
├── SacredMeshes       — 5 R3F-targeted objects (also linked in their home collections)
├── Lighting           — All light objects (stripped at GLB export)
└── Cameras            — SceneCamera
```

---

## 8. Build Order

| Phase | What Gets Built | Target Module |
|-------|----------------|---------------|
| **Phase 1** ✅ | Room shell + desk foundation + lighting mood | Done (needs fixes) |
| **Phase 2** | Fix physics violations + rebuild room correctly | Now |
| **Phase 3** | Bookshelf (left wall) + books | M4–M5 |
| **Phase 4** | Window + rain glass + curtain + city backdrop | M5 |
| **Phase 5** | Back wall — certificates, papers, sticky notes | M5 |
| **Phase 6** | Desk surface items (laptop, mug, papers, etc.) | M5–M6 |
| **Phase 7** | Sacred meshes (drone, HoloLens, arm, projector, molecule) | M6 |
| **Phase 8** | Lighting final tuning — cold blue dominant | M6 |
| **Phase 9** | UV unwrap + lightmap bake + GLB export | M7 |
| **Phase 10** | Capstone — R3F handoff, final polish | M8 |

---

## 9. Naming Conventions

- **PascalCase** for all objects: `MainDesk`, `HologramMolecule`
- **Mat_** prefix for materials: `Mat_DeskOak`
- **Tex_** prefix for textures: `Tex_Atlas_Environment`
- Sacred mesh names match exactly what R3F will call via `scene.getObjectByName()`
- No spaces, no special characters in any object name

---

## 10. Physics Rules (from Inspector Report)

Every object must satisfy:
1. **No floating** — Z_bottom of every object ≥ Z_top of the surface it rests on
2. **No embedding** — objects must not sink into surfaces they rest on
3. **Full parenting** — all desk items parented to `MainDesk`; all lamp parts to `DeskLampBase`; all shelf items to their shelf unit
4. **Wall coverage** — all walls span full 3m height (Z: 0 → 3)
5. **Desk legs** — span from floor (Z=0) to desk underside (Z≈0.73)

---

## 11. Reference Files

| File | Location |
|------|----------|
| Reference image | Shared in chat (2026-06-09) |
| Video intro | `C:\Users\ARVR\Downloads\can_you_make_look_more_gloomy_.mp4` |
| Video frames | `experiments/video_frames/frame_00..04_*.png` |
| Original spec | `C:\Users\ARVR\Documents\ARVRProjects\Portfolio\blender_scene_spec.md` |
| Detailed spec | `C:\Users\ARVR\Documents\ARVRProjects\Portfolio\blender_scene_spec_detailed.md` |
| Blend file | `PortfolioStage.blend` |
