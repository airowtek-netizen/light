import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the inline color for map, envelope, and phone icons in the footer
    content = re.sub(
        r'<i class="fas fa-map-marker-alt" style="color:#ffffff"></i>',
        r'<i class="fas fa-map-marker-alt" style="color:#00d4a3"></i>',
        content
    )
    content = re.sub(
        r'<i class="fas fa-envelope" style="color:#ffffff"></i>',
        r'<i class="fas fa-envelope" style="color:#00d4a3"></i>',
        content
    )
    content = re.sub(
        r'<i class="fas fa-phone" style="color:#ffffff"></i>',
        r'<i class="fas fa-phone" style="color:#00d4a3"></i>',
        content
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated footer icons color to #00d4a3 in all HTML files.")
