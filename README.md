# Daisy UI Component Scraper
A simple scraper for all of the Daisy UI components. This tool scrapes all of the components from the Daisy UI 5 beta library and places them into individual folders in a html file. It currently only outputs the component title, description, element preview and HTML code element.

## Prerequisites
- Python 3.8 or above
- Virtualenv

## Getting Started
Create virtual environment:
```bash
python -m virtualenv .venv
```
Start virtual environment:
```bash
source .venv/bin/activate
```
> [!NOTE]
> Use `Scripts` instead of `bin` on Windows
Install dependencies:
```bash
pip install -r requirements.txt
```
Finally, run the script with:
```bash
python daisyscrape.py
```
You will find all of the components in their respective folder in `/components`

## Changing Scraper URLs
You can run this line of javascript in `Dev Tools > Console` on a browser to get a new list of component URLs:
```javascript
[].map.call(document.querySelectorAll('#disclosure-components  a[href*="/components/"]'), x => x.href)
```
The output can be copied and pasted directly into the python file as JavaScript `Array` syntax is the same as Python `List`. Just replace the current value for `urls` on `line 5` in `daisyscrape.py` and you're good to go!
