import shapely
import geopandas


# Read Shapefile
# <class 'geopandas.geodataframe.GeoDataFrame'>
gdf = geopandas.read_file("shapefile/ne_10m_populated_places_simple.shp")

# Convert to Pandas DataFrame
# <class 'pandas.core.frame.DataFrame'>
df = gdf[['latitude', 'longitude', 'adm0name', 'name', 'scalerank', 'sov_a3', 'pop_max']]

# Filter By Pop Max
sorted_df = df.groupby(['adm0name']).apply(lambda x: x.sort_values(["pop_max"], ascending = False).head(3))

# Convert Pandas DataFrame back to GeoDataFrame
df = sorted_df
geometry = [shapely.geometry.Point(xy) for xy in zip(df.longitude, df.latitude)]
df = df.drop(['longitude', 'latitude'], axis=1)
crs = {'init': 'epsg:4326'}
gdf = geopandas.GeoDataFrame(df, crs=crs, geometry=geometry)

# Save GeoDataFrame to Shapefile
gdf.to_file("output/sorted.shp")
