import osmnx as ox
from pathlib import Path

# -------------------------
# Project root
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# IMPORTANT: Use administrative boundary
place_name = "Mumbai City, Maharashtra, India"

# Output directory
output_dir = BASE_DIR / "data/processed/osm"
output_dir.mkdir(parents=True, exist_ok=True)

# -------------------------
# 1. Ingest buildings
# -------------------------
print("Downloading OSM building footprints...")
buildings = ox.features_from_place(
    place_name,
    tags={"building": True}
)

buildings.to_file(
    output_dir / "mumbai_buildings.geojson",
    driver="GeoJSON"
)

# -------------------------
# 2. Ingest roads
# -------------------------
print("Downloading OSM road network...")
roads_graph = ox.graph_from_place(
    place_name,
    network_type="drive"
)

roads_gdf = ox.graph_to_gdfs(
    roads_graph,
    nodes=False,
    edges=True
)

roads_gdf.to_file(
    output_dir / "mumbai_roads.geojson",
    driver="GeoJSON"
)

print("✅ OSM ingestion done successfully!")
