def image_search(gdf, start_date, end_date):
    """
    Iterates through a geoDataFrame and searches Google Earth Engine
    based on certain parameters within the geoDataFrame. Buffers central
    geometery search point by 1000 meters, event date by 180 days reciprocal. 


    Parameters
    ----------
    data_file : 
        geodataframe
        start_date
        end_date

    Returns
    -------
    dataframe
        appended with imagery relative orbit number

    """

    # Set empty list
    results = []

    BASE_DATE = ee.Date(gdf['slide.date'])

    # Data search in Google Earth Engine
    im_coll = (ee.ImageCollection('COPERNICUS/S1_GRD_FLOAT')

               .filterBounds(bbox.ee)

               .filter(ee.Filter.eq('orbitProperties_pass', 'DESCENDING'))
               .filter(ee.Filter.listContains(
                   'transmitterReceiverPolarisation', 'VV'))
               .filter(ee.Filter.listContains(
                   'transmitterReceiverPolarisation', 'VH'))

                .filterDate(start_date, end_date)
                
               .map(lambda img: img.set('date', ee.Date(img.date()).format('YYYYMMdd')))
               .sort('date'))

    orbit_num = (im_coll.aggregate_array('relativeOrbitNumber_start')
             .getInfo())
    orbit_num = orbit_num[0]
    print('The Relative Orbit Number for AOI is: ', orbit_num)

    # Add new column to geopandas DataFrame for available data
    for value in orbit_num:
        if value == True:
            results.append(gdf)
        else:
            results.append('No imagery available')

    return orbit_num
