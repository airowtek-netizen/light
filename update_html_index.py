import re

def replace_svgs_by_index(filename, replacement_images):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # find all svg blocks
    pattern = r'<svg[^>]*>.*?</svg>'
    svgs = re.findall(pattern, content, flags=re.DOTALL)
    
    for i, img_tag in enumerate(replacement_images):
        if i < len(svgs):
            # Replace the first occurrence of this specific SVG
            content = content.replace(svgs[i], img_tag, 1)
            
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

services_replacements = [
    '<img src="asset/srv_pg_lidar_1790390987912.jpg" alt="LiDAR Processing" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">',
    '<img src="asset/srv_pg_ortho_1790391000853.jpg" alt="Orthophoto" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">',
    '<img src="asset/srv_pg_gis_1790391031792.jpg" alt="CAD/GIS" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">',
    '<img src="asset/srv_pg_bim_1790391043978.jpg" alt="BIM" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">',
    '<img src="asset/srv_pg_mobile_1790391057085.jpg" alt="Mobile Mapping" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">'
]
replace_svgs_by_index('c:\\DM\\Code\\light-main\\services.html', services_replacements)

industries_replacements = [
    '<img src="asset/ind_pg_urban_1790391086736.jpg" alt="Urban Planning" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">',
    '<img src="asset/ind_pg_mining_1790391098674.jpg" alt="Mining" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">',
    '<img src="asset/ind_pg_agriculture_1790391130600.jpg" alt="Agriculture" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">'
]
replace_svgs_by_index('c:\\DM\\Code\\light-main\\industries.html', industries_replacements)

print("SVGs replaced by index successfully")
