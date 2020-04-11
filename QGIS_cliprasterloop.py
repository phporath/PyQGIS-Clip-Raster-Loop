#colocar o endereço em que os arquivos estão (raster e vetor)
path = 'C:/Users/zago/mosaico/'  


#nome do arquivo vetorial
vect = iface.addVectorLayer(path + 'Nomedaaerofoto_Mosaico_Quadricula.shp', '', 'ogr')  

#nome do arquivo raster
rst = iface.addRasterLayer(path + 'Nomedaaerofoto_Mosaico_Recorte.tif', 'Nomedaaerofoto_Mosaico_Recorte.tif', 'gdal')  

#inserir o nome do mosaico para compor o nome do raster a ser recortado
nm_mosaico = 'Nomedaaerofoto_'

for feature in vect.getFeatures():
    
    row_name = feature['indice']
        
    mask_par = {
        'FIELD': 'indice', #nome do campo
        'INPUT': vect,
        'OPERATOR': 0,
        'OUTPUT': f'{path}{row_name}.shp',
        'VALUE': row_name
    }
    
    mask = processing.run("qgis:extractbyattribute", mask_par)
    
    clip_par = {
    'INPUT': rst,
    'MASK': mask['OUTPUT'],
    'NODATA': 250.0,
    'ALPHA_BAND': False,
    'CROP_TO_CUTLINE': True,
    'KEEP_RESOLUTION': True,
    'OPTIONS': None,
    'DATA_TYPE': 0,
    'OUTPUT': f'{path}'+nm_mosaico+f'{row_name}.tif'
    }
    
    clip = processing.run('gdal:cliprasterbymasklayer', clip_par)
    
print('Processo finalizado.')
