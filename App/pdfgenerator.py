PYPPETEER_CHROMIUM_REVISION = '1263111'

import asyncio
from pyppeteer import launch


async def generate_pdf(url, pdf_path):
    browser = await launch()
    page = await browser.newPage()
    
    await page.goto(url)
    
    await page.pdf({'path': pdf_path, 'format': 'A4'})
    
    await browser.close()

# Run the function


#asyncio.run(generate_pdf('file:///' + full_path, './Printables/example.pdf'))