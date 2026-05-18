import bpy

for sel in bpy.context.selected_objects:
    sel.hide_render = True