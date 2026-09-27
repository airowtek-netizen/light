import re

def update_file(filename, replacements):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for search_text, replace_text in replacements:
        # Match <svg ... </svg> where there is a specific text inside it
        # For Photogrammetry
        pattern = r'<svg[^>]*>.*?(' + search_text + r').*?</svg>'
        replacement = replace_text
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

services_replacements = [
    ('PHOTOGRAMMETRIC 3D RECONSTRUCTION', '<img src="asset/srv_pg_photogrammetry_1790390970605.jpg" alt="Photogrammetry" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">'),
    ('LiDAR POINT CLOUD PROCESSING', '<img src="asset/srv_pg_lidar_1790390987912.jpg" alt="LiDAR Processing" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">'),
    ('ORTHORECTIFIED IMAGERY GRID', '<img src="asset/srv_pg_ortho_1790391000853.jpg" alt="Orthophoto" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">'),
    ('CAD DRAFTING & GIS TOPOLOGY', '<img src="asset/srv_pg_gis_1790391031792.jpg" alt="CAD/GIS" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">'),
    ('SCAN-TO-BIM ARCHITECTURE', '<img src="asset/srv_pg_bim_1790391043978.jpg" alt="BIM" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">'),
    ('MOBILE MAPPING SYSTEM', '<img src="asset/srv_pg_mobile_1790391057085.jpg" alt="Mobile Mapping" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">')
]

update_file('services.html', services_replacements)

industries_replacements = [
    ('INFRASTRUCTURE CORRIDOR MAPPING', '<img src="asset/ind_pg_infrastructure_1790391072389.jpg" alt="Infrastructure" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">'),
    ('URBAN PLANNING & LOD2 MODELING', '<img src="asset/ind_pg_urban_1790391086736.jpg" alt="Urban Planning" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">'),
    ('MINING VOLUME CALCULATION', '<img src="asset/ind_pg_mining_1790391098674.jpg" alt="Mining" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">'),
    ('PRECISION AGRICULTURE & NDVI', '<img src="asset/ind_pg_agriculture_1790391130600.jpg" alt="Agriculture" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">')
]

update_file('industries.html', industries_replacements)
print("Updated successfully")
