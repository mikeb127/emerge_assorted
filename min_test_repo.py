import emerge as em

mm = 0.001              # meters per millimeter
model = em.Simulation('PlaneWave', loglevel='DEBUG')

hght = 60 * mm
wdth = 60 * mm
dpt = 160 * mm


air = em.geo.Box(hght, dpt, wdth,  position=(-10*mm, -100*mm, -10*mm)).background()
model.mw.set_resolution(0.2)
model.commit_geometry()
model.settings.check_ram = False
model.mw.set_frequency(10e9)

model.generate_mesh()
scat = model.mw.bc.ScatteredField(air.boundary(), power_density=13300000) #Translates to roughly 100,000 V/m

scat.set_excitations(0,90,0)

model.view(plot_mesh=True, volume_mesh=False)
model.view(bc=True)
data = model.mw.run_scattered()

model.display.add_object(air)
model.display.animate().add_field(data.field[0].cutplane(1*mm, z=12*mm).scalar('Ez','complex'), symmetrize=True)
model.display.show()