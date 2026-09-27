import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

old_block = '''        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li>Photogrammetry</li>
            <li>LiDAR Processing</li>
            <li>Orthophoto</li>
            <li>CAD / GIS</li>
            <li>Scan to BIM</li>
            <li>Mobile Mapping</li>
          </ul>
        </div>'''

new_block = '''        <div class="footer-col">
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

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try direct replacement
    if old_block in content:
        content = content.replace(old_block, new_block)
    else:
        # Fallback to regex if indentation differs
        pattern = r'<h4>Services</h4>\s*<ul>\s*<li>Photogrammetry</li>\s*<li>LiDAR Processing</li>\s*<li>Orthophoto</li>\s*<li>CAD / GIS</li>\s*<li>Scan to BIM</li>\s*<li>Mobile Mapping</li>\s*</ul>'
        replacement = '''<h4>Services</h4>
          <ul>
            <li><a href="services.html">Photogrammetry</a></li>
            <li><a href="services.html">LiDAR Processing</a></li>
            <li><a href="services.html">Orthophoto</a></li>
            <li><a href="services.html">CAD / GIS</a></li>
            <li><a href="services.html">Scan to BIM</a></li>
            <li><a href="services.html">Mobile Mapping</a></li>
          </ul>'''
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated footer links in all HTML files.")
