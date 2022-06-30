import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame
from shapely.geometry import Point


def create_geodataframe(data_file):
    """
    Reads a csv file into a GeoPandas DataFrame. Sets the index to the 'slide.id'
    and sorts the geoDataFrame by the new index. Converts the date+time column to
    a timezone aware DateTime object. Inserts two columns DateTime columns to
    that are 180 days left and right of event date. Adds a column to combine 
    reported coordinates into a list. Converts the reported  coordinates to 
    a geoPandas geometry point.

    Parameters
    ----------
    data_file : str

    Returns
    -------
    dataframe
        sorted by index
    """

    gdf = gpd.read_file(data_file)

    # Add event point column as tuple
    gdf['ctr_point'] = gdf['lon'] + ', ' + gdf['lat']

    # Convert reported coordinates to geometry
    gdf[['lon', 'lat']] = gdf[['lon', 'lat']].astype(float)
    geometry = [Point(xy) for xy in zip(gdf.lon, gdf.lat)]
    gdf = GeoDataFrame(gdf, crs="EPSG:4326", geometry=geometry)

    return gdf
