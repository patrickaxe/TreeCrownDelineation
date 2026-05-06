# Create a new env and build a new environment
cd .\TreeCrownDelineation\run
conda create -n <env-name>
conda activate <env-name>
conda env export --no-builds > environment.yml

mkdir .\training\
mkdir .\training\data\
mkdir .\training\data\tiles\
mkdir .\training\data\masks\
mkdir .\training\data\outlines\
mkdir .\training\data\dist_trafo\
mkdir .\training\data\polygons\
mkdir .\out
mkdir .\out\models
mkdir .\out\logs


# Install this package
cd .\TreeCrownDelineation
# Run the package installation, which will also install the dependencies
python ./setup.py install

# Preparation  


Save the img raster under `./run/training`
Save polygons under `./run/training/data/polygons/`



# 1 clip images to tiles

To create the raster image tiles you can either clip them using QGIS, or use the script provided in scripts/ like so:

```bash
python ./scripts/clip_image.py -i ./training/K2-21_GDA94_MGA52.tif -o ./training/data/tiles/tile_ -shp ./training/data/polygons/set1.shp
```

# 2 rasterize the delineated tree crowns
Now we rasterize the delineated tree crowns:
```bash
python ./scripts/run_rasterize.py
```

# 3 outlines
Now the outlines, very similar:
```bash
python ./scripts/run_outlines.py
```

# 4 distance transform
And lastly, the distance transform:
```bash
python ./scripts/run_dist_trafo.py

```


# 5 Start with training.ipynb

Open `.\run\training.ipynb`


# 6 Using pre-trained models， produce `output_prediction.gpkg`

```bash
cd ./run # back to the root dir
python ./scripts/inference.py -h # check the params
python ./scripts/inference.py -i ./training/K2-21_GDA94_MGA52.tif -o ./out/output_prediction.gpkg -m "./training/TCD_weights/TCD_weights/tcd-20cm-RGBI-v1.0/Unet-resnet18_epochs=209_lr=0.0001_width=224_bs=32_divby=255_custom_color_augs_k=0_jitted.pt" "./training/TCD_weights/TCD_weights/tcd-20cm-RGBI-v1.0/Unet-resnet18_epochs=209_lr=0.0001_width=224_bs=32_divby=255_custom_color_augs_k=1_jitted.pt" "./training/TCD_weights/TCD_weights/tcd-20cm-RGBI-v1.0/Unet-resnet18_epochs=209_lr=0.0001_width=224_bs=32_divby=255_custom_color_augs_k=2_jitted.pt"  "./training/TCD_weights/TCD_weights/tcd-20cm-RGBI-v1.0/Unet-resnet18_epochs=209_lr=0.0001_width=224_bs=32_divby=255_custom_color_augs_k=3_jitted.pt"  "./training/TCD_weights/TCD_weights/tcd-20cm-RGBI-v1.0/Unet-resnet18_epochs=209_lr=0.0001_width=224_bs=32_divby=255_custom_color_augs_k=4_jitted.pt" --ndvi --red 0 --nir 3 --div 255
```


# 7 Application
```bash
python ./scripts/inference.py -i ./training/K2-21_GDA94_MGA52.tif -o ./out/output_block21.gpkg -m "./out/models/Block21/Unet-resnet18_epochs=89_lr=0.0003_width=256_bs=16_jitted.pt" --div 255 --sigma 3 -l 0.4 -b 0.3 --min-dist 10 -s 0.5


python ./scripts/inference.py -i ./training/K2-21_GDA94_MGA52.tif -o ./out/output_block21_v2.gpkg -m "./out/models/Block21/Unet-resnet18_epochs=89_lr=0.0003_width=256_bs=16_jitted.pt"  -l 0.1 -b 0.1 --min-dist 5 -s 0.3

```