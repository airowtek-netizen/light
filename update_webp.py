import os
import re

files_to_update = [f for f in os.listdir('.') if f.endswith('.html')] + ['style.css']

for file in files_to_update:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace .jpg and .png with .webp
    content = content.replace('.jpg', '.webp')
    content = content.replace('.png', '.webp')
    
    # Also handle capitalized extensions just in case
    content = content.replace('.JPG', '.webp')
    content = content.replace('.PNG', '.webp')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated image extensions to .webp in {len(files_to_update)} files.")
