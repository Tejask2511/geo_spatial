# geo_spatial

## Data Download Instructions (Manual)

This project expects raw data to be downloaded manually from official sources to ensure correctness, licensing compliance, and reproducibility.

---

## DEM Download (SRTM – NASA)

**Source:** USGS EarthExplorer  
**Website:** https://earthexplorer.usgs.gov/

### Steps

1. Open the website:  
   https://earthexplorer.usgs.gov/

2. Create a **free USGS account** and log in.

3. In the **Search Criteria** tab:
   - Search location: type **Mumbai**
   - Or use map to draw/select region

4. Go to **Data Sets** tab:
   - Expand **Digital Elevation**
   - Select **SRTM**
   - Choose **SRTM 1 Arc-Second Global**

5. Click **Results**
6. Download the **`.tif`** file

### Store file at
data/raw/dem/

---

## Satellite Imagery Download (Sentinel-2 L2A)

**Source:** Copernicus Data Space  
**Website:** https://dataspace.copernicus.eu/

### Steps

1. Open the website:  
   https://dataspace.copernicus.eu/

2. Create a **free Copernicus account** and log in.

3. Search location:
   - Type **Mumbai**
   - Or select region on the map

4. Select product:
   - **Sentinel-2**
   - **Level-2A (L2A)**

5. Choose a cloud-free acquisition date

6. Download the product

### You will get
- Multiple `*.jp2` files (bands)

### Store files at
data/raw/satellite/

---

## OpenStreetMap (OSM) Download

**Source:** Geofabrik  
**Website:** https://download.geofabrik.de/

### Steps

1. Open the website:  
   https://download.geofabrik.de/

2. Navigate through:
Asia → India → Maharashtra

3. Download one of the following:
   - `*.osm.pbf` (recommended)
   - or `*.geojson`

### Store file at
data/raw/osm/

---

