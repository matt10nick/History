# History Cards Project

## Overview

This project is a collection of Python scripts for creating history cards. Images are processed and turned into printable PDF files that have 4 cards per page. Those cards can be cut out. The cards have a description on the front, and a description + date on the back. 

The description and date used come from the name of the file, in the format: description-date.jpg

The images must be 1792x2304 pixels. 

Right now, the text is added to the images via image manipulation. This is slow but tends to be fine as long as the code is running on a local machine with plenty of power. Adding the text via HTML / CSS would have better performance. However, this could complicate PDF generation and would require careful testing.   

## ToDo

- Support multiple image resolutions 
- Print all the cards in a single PDF file. 
- Dynamically generate HTML
- Add text to images via dynamic HTML and CSS

## Usage

This code was written in VS Code. A launch.json is included that will run the current file, or the app in the debugger. 

To use these scripts, you need to have Python, pyppeteer, and the Pillow library installed. 

```shell
pip install pillow
pip install pyppeteer

``` 
Please note, pyppeteer attempts to download chromium. However, that version may not be avaliable. You may have to override this by setting a system variables, or overriding the library code.  