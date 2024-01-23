# Using Optical Character recognition with HeadSpin & Appium

## Problem:

- Some applications do not expose XML or UI elements to Appium which makes automating against them challenging in both navigating and running assertions to verify features.  Using the Appium OCR plugin can help with this.
- The OCR plugin can read detect text that the base Appium library can not, which you can then manipulate in various ways to write your tests.

## Prerequisites

Before you begin, ensure you have the following prerequisites:

- [Python](https://www.python.org/downloads/) 
- [Appium 2.0](https://github.com/appium/appium)
- [Appium OCR plugin installed](https://github.com/jlipps/appium-ocr-plugin) 


## Setting up the Environment Variable

1. Open your terminal.

2. Use the following command to set the `HS_TOKEN` environment variable:

   ```bash
   export HS_TOKEN="your_token_value_here"

3. Use the following command to run the script:

   ```bash
   python appiumocr.py
