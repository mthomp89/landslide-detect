class BBox:
    """Bounding box available in many formats"""
    def __init__(self, minx, miny, maxx, maxy):
        self.minx, self.miny = (minx, miny)
        self.maxx, self.maxy = (maxx, maxy)
        self.box = sgeo.box(minx=minx, miny=miny, maxx=maxx, maxy=maxy)
        self.coords = list(self.box.exterior.coords)
        self.ee = ee.Geometry.Polygon(self.coords)
        self.geojson = self.box.__geo_interface__
        self.folium = folium.GeoJson(self.geojson)
        self.folium_bounds = [(y, x) for (x, y) in self.coords]