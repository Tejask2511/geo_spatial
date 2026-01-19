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

## How to Run the Data Ingestion Engine

### Prerequisites

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project

#### Option 1: Run All Data Types (Recommended)

```bash
python scripts/ingest.py --place "Mumbai City, Maharashtra, India"
```

This will ingest:
- DEM data (from `data/raw/dem/`)
- Satellite data (from `data/raw/satellite/`)
- OSM Buildings, Roads, and Water (downloaded from OpenStreetMap)

#### Option 2: Run Individual Modules

**DEM only:**
```bash
python scripts/ingest.py --dem-only --dem-file path/to/dem.tif
```

**Satellite only:**
```bash
python scripts/ingest.py --satellite-only --satellite-file path/to/satellite.jp2
```

**OSM only:**
```bash
python scripts/ingest.py --osm-only --place "Mumbai City, Maharashtra, India"
```

#### Option 3: Run Individual Scripts Directly

**DEM ingestion:**
```bash
python scripts/dem_ingest.py --source SRTM
```

**Satellite ingestion:**
```bash
python scripts/satellite_ingest.py --file path/to/satellite.jp2
```

**OSM ingestion:**
```bash
python scripts/osm_ingest.py --place "Mumbai City, Maharashtra, India"
```

### Command Line Arguments

#### Main Script (`ingest.py`)
- `--place` - Place name for OSM data (default: "Mumbai City, Maharashtra, India")
- `--dem-file` - Path to DEM file (optional, will auto-detect if not provided)
- `--satellite-file` - Path to satellite file (optional, will auto-detect if not provided)
- `--dem-only` - Ingest DEM only
- `--satellite-only` - Ingest satellite only
- `--osm-only` - Ingest OSM only

#### DEM Script (`dem_ingest.py`)
- `--file` - Path to DEM file (optional)
- `--source` - Data source: SRTM or Copernicus (default: SRTM)

#### Satellite Script (`satellite_ingest.py`)
- `--file` - Path to satellite file (optional)

#### OSM Script (`osm_ingest.py`)
- `--place` - Place name (required)
- `--skip-buildings` - Skip building ingestion
- `--skip-roads` - Skip road ingestion
- `--skip-water` - Skip water feature ingestion

### Example Commands

**Full ingestion:**
```bash
cd geo_spatial
python scripts/ingest.py --place "Mumbai City, Maharashtra, India"
```

**Custom place:**
```bash
python scripts/ingest.py --place "New York City, New York, USA"
```

**With specific files:**
```bash
python scripts/ingest.py --place "Mumbai City, Maharashtra, India" --dem-file data/raw/dem/custom_dem.tif --satellite-file data/raw/satellite/custom_satellite.jp2
```

### Output

After running, check:
- `data/raw/dem/` - DEM files and metadata
- `data/raw/satellite/` - Satellite files and metadata
- `data/raw/osm/` - OSM GeoJSON files and metadata
- `data/raw/metadata.json` - Consolidated metadata for all files

### Troubleshooting

**If dependencies are missing:**
```bash
pip install -r requirements.txt
```

**If OSM download fails:**
- Check internet connection
- Verify place name is correct
- Try a different place name

**If file not found:**
- Ensure raw data files are in the correct directories
- Check file paths are correct
- Verify file formats are supported (.tif, .jp2, .geojson)

---
