import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling
from pathlib import Path

# --------------------------------------------------
# 1. Resolve project root safely
#    Assumes structure:
#    geo_project/
#      ├── scripts/
#      │     └── dem_ingest.py
#      └── data/
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[1]

# --------------------------------------------------
# 2. INPUT: DEM file path
# --------------------------------------------------
raw_dem = BASE_DIR / "data" / "raw" / "dem" / "mumbai_dem.tif"

# --------------------------------------------------
# 3. OUTPUT: processed DEM file path
# --------------------------------------------------
processed_dem = BASE_DIR / "data" / "processed" / "dem" / "mumbai_dem_4326.tif"

# --------------------------------------------------
# 4. Pre-flight checks (VERY IMPORTANT)
# --------------------------------------------------
print("📂 Project Root:", BASE_DIR)
print("📄 DEM Path:", raw_dem)

if not raw_dem.exists():
    raise FileNotFoundError(
        f"\n❌ DEM file not found!\n"
        f"Expected at:\n{raw_dem}\n\n"
        f"✔ Check filename\n"
        f"✔ Check folder name (dem)\n"
        f"✔ Ensure DEM is extracted (.tif, not .zip)\n"
    )

# Create output directory
processed_dem.parent.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# 5. Read DEM, detect CRS, reproject to EPSG:4326
# --------------------------------------------------
with rasterio.open(raw_dem) as src:
    if src.crs is None:
        raise ValueError("❌ DEM has no CRS defined. Cannot reproject.")

    print("🛰️ Original CRS:", src.crs)

    transform, width, height = calculate_default_transform(
        src.crs,
        "EPSG:4326",
        src.width,
        src.height,
        *src.bounds
    )

    metadata = src.meta.copy()
    metadata.update({
        "crs": "EPSG:4326",
        "transform": transform,
        "width": width,
        "height": height
    })

    with rasterio.open(processed_dem, "w", **metadata) as dst:
        for band in range(1, src.count + 1):
            reproject(
                source=rasterio.band(src, band),
                destination=rasterio.band(dst, band),
                src_transform=src.transform,
                src_crs=src.crs,
                dst_transform=transform,
                dst_crs="EPSG:4326",
                resampling=Resampling.nearest
            )

print("✅ DEM ingestion & reprojection completed successfully")
print("📦 Output written to:", processed_dem)
