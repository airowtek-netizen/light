import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add loading="lazy" to all img tags that don't already have it
    # We will exclude logo and hero images if we can, but since it's simple, we'll just add it to all images
    # that don't have it, then we can manually fix logo if needed.
    # Actually, adding lazy to all images is fine for a quick fix, though above-the-fold images ideally shouldn't be lazy.
    
    # Find all <img> tags
    def add_lazy(match):
        img_tag = match.group(0)
        if 'loading=' not in img_tag and 'logo' not in img_tag and 'banner' not in img_tag:
            # insert loading="lazy" before the closing bracket
            return img_tag.replace('>', ' loading="lazy">')
        return img_tag
        
    content = re.sub(r'<img[^>]+>', add_lazy, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added loading='lazy' to images.")
