import re

with open('industries.html', 'r', encoding='utf-8') as f:
    content = f.read()

search_text = 'INFRASTRUCTURE CORRIDOR'
pattern = r'<svg[^>]*>.*?(' + search_text + r').*?</svg>'
match = re.search(pattern, content, flags=re.DOTALL)
if match:
    print("Found match!")
    # replace
    content = re.sub(pattern, '<img src="asset/ind_pg_infrastructure_1790391072389.jpg" alt="Infrastructure" style="width:100%; height:100%; object-fit:cover; border-radius:12px;">', content, flags=re.DOTALL)
    with open('industries.html', 'w', encoding='utf-8') as f:
        f.write(content)
else:
    print("No match for:", search_text)

