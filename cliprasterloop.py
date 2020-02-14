from qgis.core import *
from qgis.gui import *
import processing   
from processing.core.Processing import Processing
import gdal

camada_vetorial = QgsVectorLayer('C:/Users/phpor/Desktop/teste/quad2.shp','quad2.shp','ogr')
camada_raster = QgsRasterLayer('C:/Users/phpor/Desktop/aerofoto.tif','aerofoto.tif')

if camada_raster.isValid():
    print("ok")
else:
    print("not ok")

Processing.initialize()

feicao_info = camada_vetorial.getFeatures()
for feicao in feicoes:
    nome_feicao = feicao['indice']
    output_file = "C:/Users/phpor/Desktop/teste/" + "cliped_" + str(nome_feicao) + ".tif" 
    #teste = camada_vetorial.setSubsetString("indice=" + str(feicao['indice']))
    camada_vetorial.setSubsetString(f""" "indice" = '{nome_feicao}' """)

    parameters = {'INPUT': camada_raster,
            'MASK': camada_vetorial,
            'NODATA': 250.0,
            'ALPHA_BAND': False,
            'CROP_TO_CUTLINE': True,
            'KEEP_RESOLUTION': True,
            'OPTIONS': None,
            'DATA_TYPE': 0,
            'OUTPUT': output_file}
            
    print(nome_feicao)
    
    clip = processing.run('gdal:cliprasterbymasklayer', parameters)
    
    camada_vetorial.setSubsetString('')

print("done")
    
    
