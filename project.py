from manim import *

class ArcScene(Scene):
    def construct(self):
        arc = Arc(radius=2, angle=PI/6)
        self.time = 0
        self.current_angle = PI / 6  # Variable para rastrear el ángulo actual del arco
        
        def update_arc(arc, dt):
            self.time += dt
            self.current_angle += 0.5 * dt  # Incrementa el ángulo a medida que pasa el tiempo
            
            print(arc.angle)
            print(arc.start_angle)
            # Reemplaza el arco con uno nuevo usando el ángulo actualizado
            if arc.angle ==arc.start_angle:
                self.current_angle = 0
            arc.become(Arc(radius=2, angle=self.current_angle, start_angle=self.current_angle*2))
            # print(self.current_angle)
        
        arc.add_updater(update_arc)
        self.add(arc)
        self.wait(17)
