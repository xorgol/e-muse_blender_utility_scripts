import bpy
for obj in bpy.data.objects:
    if obj.type == 'MESH':
        if len(obj.material_slots) == 0:
            obj.select_set(True)
        else:
            mat = any(slot for slot in obj.material_slots if slot.material)
            obj.select_set(not bool(mat))