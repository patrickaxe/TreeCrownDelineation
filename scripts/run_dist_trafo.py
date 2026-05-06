import glob, subprocess, sys

tiles = sorted(glob.glob('./training/data/tiles/*.tif'))
cmd = [sys.executable, './scripts/rasterize_to_distance_transform.py', '-i'] + tiles + [
    '-o', './training/data/dist_trafo/dist_trafo_',
    '-shp', './training/data/polygons/set1.shp'
]
subprocess.run(cmd)