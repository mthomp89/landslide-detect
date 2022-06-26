import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame
from shapely.geometry import Point


def create_dataframe(data_file):
    """
    Reads a csv file into a GeoPandas DataFrame. Sets the index to the 'slide.id'
    and sorts the geoDataFrame by the new index. Converts the date+time column to
    a timezone aware DateTime object. Inserts two columns DateTime columns to
    that are 180 days left and right of event date. Adds a column to combine 
    reported coordinates into a list. Converts the reported  geocoordinates to 
    a geoPandas geometry point.

    Parameters
    ----------
    data_file : str

    Returns
    -------
    dataframe
        sorted by index
    """

    gdf = gpd.read_file(data_file,
                        index_col='slide.id',
                        parse_dates=['slide.date'])

    gdf = gdf.drop(['slide.index'], axis=1)

    # Convert to DatTime object
    gdf['slide.date'] = pd.to_datetime(gdf['slide.date'])
    gdf['slide.date'] = gdf['slide.date'].dt.date

    # Insert columns for date range
    gdf.insert(loc=2, column='pre_event',
               value=gdf['slide.date'] - pd.Timedelta(days=180))
    gdf.insert(loc=3, column='post_event',
               value=gdf['slide.date'] + pd.Timedelta(days=180))

    # Add event point column as tuple
    gdf['ctr_point'] = gdf['lon'] + ', ' + gdf['lat']

    # Convert reported geocoordinates to geometery
    gdf[['lon', 'lat']] = gdf[['lon', 'lat']].astype(float)
    geometry = [Point(xy) for xy in zip(gdf.lon, gdf.lat)]
    gdf = GeoDataFrame(gdf, crs="EPSG:4326", geometry=geometry)

    return gdf
