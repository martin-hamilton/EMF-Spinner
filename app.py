import app
import math
import time
from events.input import Buttons, BUTTON_TYPES
from app_components import clear_background

class EMF_Spinner(app.App):
    def __init__(self):
        self.button_states = Buttons(self)
        self.x = -240
        self.r = 0

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

    def draw(self, ctx):
        clear_background(ctx)
        ctx.save()
        # this seems very resource intensive - perhaps we can avoid redrawing with each rotation of the EMF logo?
        ctx.linear_gradient(-120,-120,240,240)
        if self.r in range(0,89):
            ctx.add_stop(0.0, (46,173,217), 1.0)
            ctx.add_stop(0.5, (249,226,0), 1.0)
        elif self.r in range(90,179):
            ctx.add_stop(0.0, (249,226,0), 1.0)
            ctx.add_stop(0.5, (246,127,2), 1.0)
        elif self.r in range(180,269):
            ctx.add_stop(0.0, (246,127,2), 1.0)
            ctx.add_stop(0.5, (245,80,137), 1.0)
        else:
            ctx.add_stop(0.0, (245,80,137), 1.0)
            ctx.add_stop(0.5, (46,173,217), 1.0)
        ctx.rectangle(-120, -120, 240, 240)
        ctx.fill()
        # yellow circle around the edge of the screen
        ctx.rgb(255,234,0).arc(0,0,120,0,2*math.pi, True).stroke()
        ctx.rotate((self.r*math.pi)/180)
        ctx.image("/apps/martin_hamilton_EMF_Spinner/emf2024-logo-dark-small.png",self.x,-120,133,235)
        self.r = self.r + 10
        if (self.r > 360):
            self.r = 0
        if (self.x < -70):
            self.x = self.x + 10
        time.sleep(0.01)

__app_export__ = EMF_Spinner

