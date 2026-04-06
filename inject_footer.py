import os, re

files = ['index.html', 'about.html', 'services.html', 'industries.html', 'contact.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extract the footer tag contents
    footer_match = re.search(r'(<footer>.*</footer>)', html, re.DOTALL)
    if not footer_match:
        print(f"Skipping {file}, no footer found.")
        continue
    
    footer_content = footer_match.group(1)
    
    # Remove the whole template wrapper
    html = re.sub(r'<template id="footer-template">\s*<footer>.*?</footer>\s*</template>', '', html, flags=re.DOTALL)
    
    # Replace <footer-component> with the footer HTML
    html = re.sub(r'<footer-component>\s*</footer-component>', footer_content, html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Footer injected directly into all files.")
