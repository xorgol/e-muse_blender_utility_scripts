import bpy

index = 0
renameTo = "Pippo"

for sel in bpy.context.selected_objects:
    sel.name = renameTo + str(index)
    index += 1