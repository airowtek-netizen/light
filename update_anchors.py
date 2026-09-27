# -*- coding: utf-8 -*-
import os
import re

# 1. Add IDs to services.html
with open('services.html', 'r', encoding='utf-8') as f:
    services_content = f.read()

# Replace using regex to find the section tags
# SERVICE 1: Photogrammetry
services_content = re.sub(
    r'(<!-- SERVICE 1.*?-->\s*)<div style="max-width:1200px;margin:0 auto;padding:80px 4%">',
    r'\1<div id="photogrammetry" style="max-width:1200px;margin:0 auto;padding:80px 4%">',
    services_content, count=1, flags=re.DOTALL
)

# SERVICE 2: LiDAR
services_content = re.sub(
    r'(<!-- SERVICE 2.*?-->\s*)<div style="max-width:1200px;margin:0 auto;padding:80px 4%">',
    r'\1<div id="lidar" style="max-width:1200px;margin:0 auto;padding:80px 4%">',
    services_content, count=1, flags=re.DOTALL
)

# SERVICE 3: Orthophoto
services_content = re.sub(
    r'(<!-- SERVICE 3.*?-->\s*)<div style="max-width:1200px;margin:0 auto;padding:80px 4%">',
    r'\1<div id="orthophoto" style="max-width:1200px;margin:0 auto;padding:80px 4%">',
    services_content, count=1, flags=re.DOTALL
)

# SERVICE 4: CAD/GIS
services_content = re.sub(
    r'(<!-- SERVICE 4.*?-->\s*)<div style="max-width:1200px;margin:0 auto;padding:80px 4%">',
    r'\1<div id="cad-gis" style="max-width:1200px;margin:0 auto;padding:80px 4%">',
    services_content, count=1, flags=re.DOTALL
)

# SERVICE 5: BIM
services_content = re.sub(
    r'(<!-- SERVICE 5.*?-->\s*)<div style="max-width:1200px;margin:0 auto;padding:80px 4%">',
    r'\1<div id="bim" style="max-width:1200px;margin:0 auto;padding:80px 4%">',
    services_content, count=1, flags=re.DOTALL
)

# SERVICE 6: MOBILE MAPPING
services_content = re.sub(
    r'(<!-- SERVICE 6.*?-->\s*)<div style="max-width:1200px;margin:0 auto;padding:80px 4%">',
    r'\1<div id="mobile-mapping" style="max-width:1200px;margin:0 auto;padding:80px 4%">',
    services_content, count=1, flags=re.DOTALL
)

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(services_content)


# 2. Update all footers
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

old_footer_block = '''        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="services.html">Photogrammetry</a></li>
            <li><a href="services.html">LiDAR Processing</a></li>
            <li><a href="services.html">Orthophoto</a></li>
            <li><a href="services.html">CAD / GIS</a></li>
            <li><a href="services.html">Scan to BIM</a></li>
            <li><a href="services.html">Mobile Mapping</a></li>
          </ul>
        </div>'''

new_footer_block = '''        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="services.html#photogrammetry">Photogrammetry</a></li>
            <li><a href="services.html#lidar">LiDAR Processing</a></li>
            <li><a href="services.html#orthophoto">Orthophoto</a></li>
            <li><a href="services.html#cad-gis">CAD / GIS</a></li>
            <li><a href="services.html#bim">Scan to BIM</a></li>
            <li><a href="services.html#mobile-mapping">Mobile Mapping</a></li>
          </ul>
        </div>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_footer_block in content:
        content = content.replace(old_footer_block, new_footer_block)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

# 3. Update script.js searchData
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace("{ title: 'Photogrammetry', category: 'Services', url: 'services.html' }", "{ title: 'Photogrammetry', category: 'Services', url: 'services.html#photogrammetry' }")
js = js.replace("{ title: 'LiDAR Processing', category: 'Services', url: 'services.html' }", "{ title: 'LiDAR Processing', category: 'Services', url: 'services.html#lidar' }")
js = js.replace("{ title: 'Orthophoto', category: 'Services', url: 'services.html' }", "{ title: 'Orthophoto', category: 'Services', url: 'services.html#orthophoto' }")
js = js.replace("{ title: 'CAD / GIS', category: 'Services', url: 'services.html' }", "{ title: 'CAD / GIS', category: 'Services', url: 'services.html#cad-gis' }")
js = js.replace("{ title: 'Scan to BIM', category: 'Services', url: 'services.html' }", "{ title: 'Scan to BIM', category: 'Services', url: 'services.html#bim' }")
js = js.replace("{ title: 'Mobile Mapping', category: 'Services', url: 'services.html' }", "{ title: 'Mobile Mapping', category: 'Services', url: 'services.html#mobile-mapping' }")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated IDs, footers, and script.js!")
