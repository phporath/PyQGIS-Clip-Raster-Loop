from qgis.core import *
from qgis.gui import *
import processing   
from processing.core.Processing import Processing
import gdal

VECTOR = QgsVectorLayer('C:/Users/phpor/Desktop/teste/quad2.shp','quad2.shp','ogr')

RASTER = QgsRasterLayer('C:/Users/phpor/Desktop/aerofoto.tif','aerofoto.tif')
if RASTER.isValid():
    print("ok")
else:
    print("not ok")

Processing.initialize()

row_info = VECTOR.getFeatures()
for row in row_info:
    row_name = row['indice']
    output_file = "C:/Users/phpor/Desktop/teste/" + "cliped_" + str(row['indice']) + ".tif"
    teste = VECTOR.setSubsetString("indice=" + str(row['indice']))
        
    parameters = {'INPUT': RASTER,
            'MASK': VECTOR,
            'NODATA': 250.0,
            'ALPHA_BAND': False,
            'CROP_TO_CUTLINE': True,
            'KEEP_RESOLUTION': True,
            'OPTIONS': None,
            'DATA_TYPE': 0,
            'OUTPUT': output_file}
            
    print(row_name)
    
    clip = processing.run('gdal:cliprasterbymasklayer', parameters)
    
    VECTOR.setSubsetString('')

print("done")
    
    