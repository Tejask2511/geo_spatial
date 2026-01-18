import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling
from pathlib import Path
import os

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

raw_sat = BASE_DIR / "data/raw/satellite/mumbai_satellite.jp2"
processed_sat = BASE_DIR / "data/processed/satellite/mumbai_satellite_4326.tif"

os.makedirs(processed_sat.parent, exist_ok=True)

with rasterio.open(raw_sat) as src:
    print("Original CRS:", src.crs)

    transform, width, height = calculate_default_transform(
        src.crs, "EPSG:4326",
        src.width, src.height,
        *src.bounds
    )

    kwargs = src.meta.copy()
    kwargs.update({
        "crs": "EPSG:4326",
        "transform": transform,
        "width": width,
        "height": height
    })

    with rasterio.open(processed_sat, "w", **kwargs) as dst:
        for i in range(1, src.count + 1):
            reproject(
                source=rasterio.band(src, i),
                destination=rasterio.band(dst, i),
                src_transform=src.transform,
                src_crs=src.crs,
                dst_transform=transform,
                dst_crs="EPSG:4326",
                resampling=Resampling.nearest
            )

print("✅ Satellite ingestion and CRS normalization done!")
