import base64, math, cairosvg
from fontTools.pens.boundsPen import BoundsPen
from arc import ArcText
from PIL import Image
import numpy as np, io

SRC = '/mnt/user-data/uploads/Gemini_Generated_Image_8sapbt8sapbt8sap.jpg'
b64 = base64.b64encode(open(SRC, 'rb').read()).decode()
CX, CY = 704, 386
CREAM, INK, ACC = "#F2ECE1", "#131417", "#FF5A2D"
BAND_MID = 292

top = ArcText('fonts/LuckiestGuy-Regular.ttf')
bot = ArcText('fonts/ArchivoBlack-Regular.ttf')

def cap(at):
    bp = BoundsPen(at.gs); at.gs[at.cmap[ord('T')]].draw(bp); return bp.bounds[3]/at.upem

tcr, bcr = cap(top), cap(bot)
TS, TSP = 46/tcr, 6
BS, BSP = 34, 4
TR = BAND_MID - (tcr*TS)/2
BR = BAND_MID + (bcr*BS)/2

tp = top.paths('TILLAS LAB', TS, TSP, CX, CY, TR, 270, +1)
bp = bot.paths('LIMPIAS · FRESCAS · IMPECABLES', BS, BSP, CX, CY, BR, 90, -1)
kt, kb = TS/1000, BS/1000

def layer(paths, k, fill, stroke=None, sw=0, dx=0, dy=0):
    s = f' stroke="{stroke}" stroke-width="{sw/k:.1f}" stroke-linejoin="round" stroke-linecap="round"' if stroke else ''
    inner = "".join(f'<path d="{d}" transform="{tr}" fill="{fill}"{s}/>' for d, tr in paths)
    return f'  <g transform="translate({dx},{dy})">{inner}</g>'

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
 viewBox="324 6 760 760" width="760" height="760">
  <image x="0" y="0" width="1408" height="768" xlink:href="data:image/jpeg;base64,{b64}"/>
{layer(tp,kt,INK,INK,32,6,8)}
{layer(tp,kt,ACC,ACC,32)}
{layer(tp,kt,INK,INK,19)}
{layer(tp,kt,CREAM)}
{layer(bp,kb,INK)}
</svg>'''
open('pack/Logo/tillas-lab-logo.svg','w').write(svg)
print(f"TS={TS:.1f} TR={TR:.1f} ancho={top.width('TILLAS LAB',TS,TSP):.0f} arco={2*math.pi*TR*162/360:.0f}")

png = cairosvg.svg2png(bytestring=svg.encode(), output_width=3000)
a = np.array(Image.open(io.BytesIO(png)).convert('RGBA')).astype(int)
S = a.shape[0]; c = S/2.0; R = 357.0/760*S
Y, X = np.ogrid[:S,:S]; r = np.sqrt((X-c)**2+(Y-c)**2); out = r > R+5
w = a.copy(); w[out] = [255,255,255,255]
Image.fromarray(w.astype('uint8')).save('pack/Logo/tillas-lab-logo.png')
t = a.copy(); t[out] = [0,0,0,0]; t[(r>R+1)&(r<=R+5),3] = 120
Image.fromarray(t.astype('uint8')).save('pack/Logo/tillas-lab-logo-transparente.png')
base = Image.open('pack/Logo/tillas-lab-logo.png')
for s in (512, 180):
    base.resize((s,s), Image.LANCZOS).save(f'pack/Logo/tillas-lab-perfil-{s}.png')
Image.open('pack/Logo/tillas-lab-logo.png').resize((680,680)).save('prev_final.png')
print("listo")
