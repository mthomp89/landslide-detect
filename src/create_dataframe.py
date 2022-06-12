import geopandas as gpd
from geopandas import GeoDataFrame
from shapely.geometry import Point

def create_dataframe(data_file):
    """
    Reads a csv file into a GeoPandas DataFrame. Sets the index to the 'slide.id'
    and sorts the geoDataFrame by the new index. Converts the date+time column to
    a DateTime object and drops the time. Converts the reported geocoordinates to
    a geoPandas geometry point.

    Parameters
    ----------
    data_file : str

    Returns
    -------
    dataframe
        sorted by index
    """

    gdf = gpd.read_file(data_file, index_col='slide.id').sort_values(by='slide.id')
    gdf = gdf.set_index('slide.id')
    # Convert to DatTime object, drop time
#     gdf['slide.date'] = pd.to_datetime(gdf['slide.date'])
#     gdf['slide.date'] = gdf['slide.date'].dt.date
    # Convert reported geocoordinates to geometery
    gdf[['lon', 'lat']] = gdf[['lon', 'lat']].astype(float)
    geometry = [Point(xy) for xy in zip(gdf.lon, gdf.lat)]
    gdf = GeoDataFrame(gdf, crs="EPSG:4326", geometry=geometry)

    return gdf