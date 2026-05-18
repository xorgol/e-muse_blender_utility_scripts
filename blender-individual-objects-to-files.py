import bpy
import os

# --- CONFIGURATION ---
export_path = "/Users/adriano/Developer/bccaec-gemini/oggetti_singoli2"
max_res = 1024 
image_format_setting = 'AUTO' # AUTO is safer than WEBP for debugging
use_draco_compression = True

if not os.path.exists(export_path):
    os.makedirs(export_path)

# --- 1. PROPORTIONAL TEXTURE RESIZING ---
print("Resizing textures (maintaining aspect ratio)...")
for img in bpy.data.images:
    if img.type == 'IMAGE' and img.has_data:
        width, height = img.size
        
        # Calculate new dimensions only if larger than max_res
        if width > max_res or height > max_res:
            if width >= height:
                new_w = max_res
                new_h = int((height / width) * max_res)
            else:
                new_h = max_res
                new_w = int((width / height) * max_res)
            
            try:
                img.scale(new_w, new_h)
                print(f"Resized {img.name} to {new_w}x{new_h}")
            except Exception as e:
                print(f"Failed to resize {img.name}: {e}")

# --- 2. BATCH EXPORT ---
bpy.ops.object.select_all(action='DESELECT')
mesh_objects = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH']

for obj in mesh_objects:
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    
    # We keep your "0,0,0" A-Frame workflow by NOT moving the object.
    # We only apply Rotation and Scale to keep the geometry clean.
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

    # Export
    filename = bpy.path.clean_name(obj.name) + ".glb"
    full_path = os.path.join(export_path, filename)
    
    print(f"Exporting: {filename}")
    
    bpy.ops.export_scene.gltf(
        filepath=full_path,
        export_format='GLB',
        use_selection=True,
        export_apply=True,
        export_draco_mesh_compression_enable=use_draco_compression,
        export_image_format=image_format_setting
    )
    
    obj.select_set(False)

print("--- Export Complete ---")