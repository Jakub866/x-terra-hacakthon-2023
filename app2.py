from mundilib import MundiCatalogue, MUNDI_COLLECTIONS, MUNDI_COLLECTION_IDS
from utils import height2width, clear_dir
from giflib import create_gif_from_folder

excluded_layers = ["NDVI_RAW", "SCL_RAW"]

selected_collection = MUNDI_COLLECTIONS[1]
mndi_wms = MUNDI_COLLECTION_IDS
print(f"Using {selected_collection} collection")
# Init wms
c = MundiCatalogue()
wms = c.get_collection(selected_collection).mundi_wms('L2A')
layers = list(wms.contents.keys())
print(layers)
_projection_ = 'EPSG:3857'
_bbox_ = (1.3691896336775358, 43.45076739750934, 1.550892291377437, 43.52969044787278)
# _bbox_ = (752904.7286, 5826183.1700, 819252.0692, 5871128.1426)  # geneva
_bbox_ = (-782715.1696,4945781.4782,1364859.5771,6834081.8249)
_time_ = '2022-02-10/2023-02-10'
_height_ = 1000
_width_ = height2width(_bbox_, _height_)

IMG_DIR = "gif_images/"
clear_dir(IMG_DIR)

for layer in layers:
    if layer in excluded_layers:
        print(f"{layer} layer was excluded")
        continue
    else:
        print(f"Downloading {layer} layer image")

    img_tc = wms.getmap(
        layers=[layer],
        srs=_projection_,
        bbox=_bbox_,
        size=(_width_, _height_),
        format='image/png',
        time=_time_,
        showlogo=False,
        transparent=False
    )
    out = open(f'{IMG_DIR}{layer}.png', 'wb')
    out.write(img_tc.read())
    out.close()

print("Creating gif")
create_gif_from_folder(IMG_DIR)
