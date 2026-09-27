import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

links = []

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        # Find hrefs
        hrefs = re.findall(r'href=["\'](.*?)["\']', content)
        for h in hrefs:
            links.append((file, 'href', h))
        
        # Find window.location.hrefs
        locs = re.findall(r'window\.location\.href=["\'](.*?)["\']', content)
        for l in locs:
            links.append((file, 'onclick', l))

# Group and validate
internal_files = set(html_files)
broken_internal = []
external = []
anchors = []
other = []

for file, ltype, link in links:
    if link.startswith('http'):
        external.append((file, link))
    elif link.startswith('#'):
        anchors.append((file, link))
    elif link.endswith('.html') or link.endswith('.css') or link.endswith('.js') or link.startswith('asset/'):
        # Check if exists
        target = link.split('#')[0]
        if target not in internal_files and not os.path.exists(target):
            broken_internal.append((file, link))
    else:
        other.append((file, link))

print(f"Checked {len(html_files)} HTML files.")
print(f"Found {len(links)} total links.")
print("\n--- Broken Internal Links ---")
if broken_internal:
    for f, l in set(broken_internal):
        print(f"{f}: {l}")
else:
    print("None found!")

print("\n--- External Links ---")
for f, l in set(external):
    print(f"{f}: {l}")
    
print("\n--- Unhandled/Other Links (Check manually) ---")
for f, l in set(other):
    print(f"{f}: {l}")

