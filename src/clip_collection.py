def clip_collection(image_collection, start_date, end_date, aoi):
    image_collection = (
        image_collection
        # Filter out images outside the AOI
        .filterBounds(bbox.ee)
        # Filter out images outside the date range
        .filterDate(start_date, end_date)
        # Clip each image to AOI
        .map(lambda im: im.clip(bbox.ee))
        .map((lambda img: 
             img.set('date', ee.Date(img.date()).format('YYYYMMdd'))))
        .sort('date')
    )
    return image_collection