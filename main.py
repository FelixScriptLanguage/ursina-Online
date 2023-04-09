from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
open('./wz.txt','w').write('Vec3(0, 0.00100005, 0)')
app = Ursina()
def input(key):
    if key == 'escape':
        quit()
rd = Vec3(0, 0.00100005, 0)
def update():
    if not fk.on_cooldown:
        print('ok')
        rdcontent = open('./wz.txt','r',encoding='UTF-8').read()
        try:
            fk.position = eval(rdcontent)
        except:
            pass
        open('./wzxx.txt','w',encoding='UTF-8').write(str(player.position))
        fk.on_cooldown = True
        invoke(setattr,fk,'on_cooldown',False,delay=0.2)
window.show_ursina_splash = True
window.fps_counter.enabled = False
window.exit_button.visible = False
#window.fullscreen = True


#a = EditorCamera()
player = FirstPersonController()
#player.speed = 10

ground = Entity(model = "plane", scale = (100,1,100), texture = "./sc/wl/grass.png" , texture_scale = (10, 10), collider = "box")
fk = Entity(model='./sc/r.glb',scale=4.5, position=rd,on_cooldown=False, collider = "box")
xf = Entity(model = "./sc/xf.glb", scale = 15 ,position=(0.2,0,2.5))
#for i in range(10):
t = Entity(model="./sc/tree.glb", scale=15, position=(5, 4.5,5))
sky_texture = load_texture('./sc/sky.jpg')
sky = Sky(texture=sky_texture,on_cooldown=False)
app.run()