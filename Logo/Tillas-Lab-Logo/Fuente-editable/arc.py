import math
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

class ArcText:
    def __init__(self, path):
        self.f = TTFont(path)
        self.gs = self.f.getGlyphSet()
        self.upem = self.f['head'].unitsPerEm
        self.cmap = self.f.getBestCmap()
        self.hmtx = self.f['hmtx']

    def _glyph(self, ch):
        name = self.cmap.get(ord(ch))
        if name is None: return None, 0
        pen = SVGPathPen(self.gs)
        self.gs[name].draw(pen)
        return pen.getCommands(), self.hmtx[name][0]

    def width(self, text, size, spacing):
        k = size/self.upem
        w = 0
        for ch in text:
            _, adv = self._glyph(ch)
            w += adv*k + spacing
        return w - spacing

    def paths(self, text, size, spacing, cx, cy, R, center_deg, direction):
        """direction=+1 top (glyphs outward), -1 bottom (glyphs inward)"""
        k = size/self.upem
        total = self.width(text, size, spacing)
        s = -total/2
        out = []
        for ch in text:
            d, adv = self._glyph(ch)
            gw = adv*k
            if d and ch != ' ':
                sc = s + gw/2                      # glyph centre along arc
                th = math.radians(center_deg) + direction*(sc/R)
                px = cx + R*math.cos(th)
                py = cy + R*math.sin(th)
                if direction > 0:
                    tx, ty = -math.sin(th), math.cos(th)
                else:
                    tx, ty = math.sin(th), -math.cos(th)
                ang = math.degrees(math.atan2(ty, tx))
                tr = (f"translate({px:.2f},{py:.2f}) rotate({ang:.3f}) "
                      f"scale({k:.5f},{-k:.5f}) translate({-adv/2:.1f},0)")
                out.append((d, tr))
            s += gw + spacing
        return out
