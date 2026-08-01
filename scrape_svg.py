import urllib.request
import re
import sys

year = sys.argv[1]
url = f'https://github.com/AdityaxDeore?from={year}-12-01&to={year}-12-31&tab=overview'

html = urllib.request.urlopen(url).read().decode('utf-8')
svg_match = re.search(r'<svg[^>]+js-calendar-graph-svg[^>]*>.+?</svg>', html, re.DOTALL)

if svg_match:
    svg_content = svg_match.group(0)
    # the SVG might not have xmlns attribute, so add it
    if 'xmlns="http://www.w3.org/2000/svg"' not in svg_content:
        svg_content = svg_content.replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ')
    
    with open(f'{year}.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Saved {year}.svg")
else:
    print(f"No SVG found for {year}")
