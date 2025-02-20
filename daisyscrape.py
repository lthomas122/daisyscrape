import requests
from bs4 import BeautifulSoup
import os

urls = ['https://v5.daisyui.com/components/button/',
        'https://v5.daisyui.com/components/dropdown/',
        'https://v5.daisyui.com/components/modal/',
        'https://v5.daisyui.com/components/swap/',
        'https://v5.daisyui.com/components/theme-controller/',
        'https://v5.daisyui.com/components/accordion/',
        'https://v5.daisyui.com/components/avatar/',
        'https://v5.daisyui.com/components/badge/',
        'https://v5.daisyui.com/components/card/',
        'https://v5.daisyui.com/components/carousel/',
        'https://v5.daisyui.com/components/chat/',
        'https://v5.daisyui.com/components/collapse/',
        'https://v5.daisyui.com/components/countdown/',
        'https://v5.daisyui.com/components/diff/',
        'https://v5.daisyui.com/components/kbd/',
        'https://v5.daisyui.com/components/list/',
        'https://v5.daisyui.com/components/stat/',
        'https://v5.daisyui.com/components/status/',
        'https://v5.daisyui.com/components/table/',
        'https://v5.daisyui.com/components/timeline/',
        'https://v5.daisyui.com/components/breadcrumbs/',
        'https://v5.daisyui.com/components/dock/',
        'https://v5.daisyui.com/components/link/',
        'https://v5.daisyui.com/components/menu/',
        'https://v5.daisyui.com/components/navbar/',
        'https://v5.daisyui.com/components/pagination/',
        'https://v5.daisyui.com/components/steps/',
        'https://v5.daisyui.com/components/tab/',
        'https://v5.daisyui.com/components/alert/',
        'https://v5.daisyui.com/components/loading/',
        'https://v5.daisyui.com/components/progress/',
        'https://v5.daisyui.com/components/radial-progress/',
        'https://v5.daisyui.com/components/skeleton/',
        'https://v5.daisyui.com/components/toast/',
        'https://v5.daisyui.com/components/tooltip/',
        'https://v5.daisyui.com/components/calendar/',
        'https://v5.daisyui.com/components/checkbox/',
        'https://v5.daisyui.com/components/fieldset/',
        'https://v5.daisyui.com/components/file-input/',
        'https://v5.daisyui.com/components/filter/',
        'https://v5.daisyui.com/components/label/',
        'https://v5.daisyui.com/components/radio/',
        'https://v5.daisyui.com/components/range/',
        'https://v5.daisyui.com/components/rating/',
        'https://v5.daisyui.com/components/select/',
        'https://v5.daisyui.com/components/input/',
        'https://v5.daisyui.com/components/textarea/',
        'https://v5.daisyui.com/components/toggle/',
        'https://v5.daisyui.com/components/validator/',
        'https://v5.daisyui.com/components/divider/',
        'https://v5.daisyui.com/components/drawer/',
        'https://v5.daisyui.com/components/footer/',
        'https://v5.daisyui.com/components/hero/',
        'https://v5.daisyui.com/components/indicator/',
        'https://v5.daisyui.com/components/join/',
        'https://v5.daisyui.com/components/mask/',
        'https://v5.daisyui.com/components/stack/',
        'https://v5.daisyui.com/components/mockup-browser/',
        'https://v5.daisyui.com/components/mockup-code/',
        'https://v5.daisyui.com/components/mockup-phone/',
        'https://v5.daisyui.com/components/mockup-window/'
        ]
# Step 1: Send a GET request
headers = {"User-Agent": "Mozilla/5.0"}  # Helps avoid blocks

def createFolder(name):
    directory_name = f"components/{name}"
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

for url in urls:
    response = requests.get(url, headers=headers)
    # Step 2: Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 3: Extract specific elements
    title = soup.find("h1")
    titleText = title.text.lower()
    createFolder(titleText)
    f = open(f"components/{titleText}/{titleText}.html", "a")
    f.write(f"{title}")
    p = title.find_next_sibling("p")
    f.write(f"{p}")  # Example: Extracts the first <h1> text
    previewTitles = soup.find_all("h4", class_="component-preview-title")
    for t in previewTitles:
        f.write(f"{t}")
        tab = t.parent.find_next_sibling("div", class_="tabs")
        preview = tab.find("div", class_="preview")
        code = tab.find("div", class_="code-wrapper")
        f.write(f"{preview}")
        code = f"{code}".replace('$$', '')
        f.write(f"<pre><code>{code}<code></pre>")
    
    f.close()
    
