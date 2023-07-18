from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import math


class Workspace(Widget):
    txtinpt1 = ObjectProperty(None)
    txtinpt2 = ObjectProperty(None)
    txtinpt3 = ObjectProperty(None)
    outlbl = ObjectProperty(None)

    def sub_pressed(self):
        sol = 'Sol: { Impossible }'
        a = int(self.txtinpt1.text)
        b = int(self.txtinpt2.text)
        c = int(self.txtinpt3.text)

        delta = b * b - 4 * a * c

        b = -b
        aa = 2 * a

        if delta > 0:
            sqdelta = math.sqrt(delta)
            x1 = (b + sqdelta) / aa
            x2 = (b - sqdelta) / aa
            sol = str('Sol: { ' + str(x1) + ' ; ' + str(x2) + ' }')
        elif delta == 0:
            x12 = b / aa
            sol = str('Sol: { ' + str(x12) + ' }')

        self.outlbl.text = sol


class ZeroFinderApp(App):
    def build(self):
        return Workspace()


if __name__ == '__main__':
    ZeroFinderApp().run()
