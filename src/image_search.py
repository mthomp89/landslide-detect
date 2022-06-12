def image_search(gdf):
    """
    Iterates through a geoDataFrame and searches Google Earth Engine
    based on certain parameters within the geoDataFrame. Buffers central
    geometery search point by 1000 meters, event date by 180 days reciprocal. 

    
    Parameters
    ----------
    data_file : geodataframe

    Returns
    -------
    dataframe
        appended with imagery timestamplist
    
    """

    # Set empty list
    results = []
    
    BASE_DATE = ee.Date(gdf['slide.date'])
    
    # Data search in Google Earth Engine
    im_coll = (ee.ImageCollection('COPERNICUS/S1_GRD_FLOAT')
               .filterBounds(gdf['geometry'])
               .filter(ee.Geometry.Point.buffer({'distance': 1000}))
               .filterDate(BASE_DATE, 
                           BASE_DATE.advance(-180, 'days'), 
                           BASE_DATE.advance(180, 'days'))
#                .filter(ee.Filter.eq('orbitProperties_pass', 'DESCENDING'))
               .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV'))
               .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VH'))
               .map(lambda img: img.set('date', ee.Date(img.date()).format('YYYYMMdd')))
               .sort('date'))
    timestamplist = (im_coll.aggregate_array('date')
                            .map(lambda d: ee.String('T').cat(ee.String(d)))
                            .getInfo())
    
    # Add new column to geopandas DataFrame for avaiable data
    for value in timestamplist:
        if value == True:
            results.append(timestamplist)
        else:
            results.append('No imagery available')

    return gdf