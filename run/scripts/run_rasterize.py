import glob, subprocess, sys

tiles = sorted(glob.glob('./training/data/tiles/*.tif'))
cmd = [sys.executable, './scripts/rasterize.py', '-i'] + tiles + [
    '-o', './training/data/masks/mask_',
    '-shp', './training/data/polygons/set1.shp'
]
subprocess.run(cmd)