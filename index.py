import shapely
import geopandas


# Read Shapefile
# <class 'geopandas.geodataframe.GeoDataFrame'>
geodataframe = geopandas.read_file("shapefile/ne_10m_populated_places_simple.shp")

# Convert to Pandas DataFrame
# <class 'pandas.core.frame.DataFrame'>
dataframe = geodataframe[['latitude', 'longitude', 'name', 'scalerank', 'sov_a3', 'pop_max']]

# Convert Pandas DataFrame back to GeoDataFrame
geometry = [shapely.geometry.Point(xy) for xy in zip(dataframe['longitude'], df['latitude'])]
crs = {'init': 'epsg:4326'}
geodataframe = geopandas.GeoDataFrame(dataframe, crs=crs, geometry=geometry)

# Save GeoDataFrame to Shapefile
geodataframe.to_file("output.shp")
