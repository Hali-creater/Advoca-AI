
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        try:
            await page.goto("http://localhost:8501")
            await page.wait_for_selector("h1:has-text('Advoca AI')")

            # Click the "Commercial Law" button to start the interaction
            await page.click("button:has-text('Commercial Law')")

            # Wait for the first question to ensure the app has responded
            await page.wait_for_selector("text=What type of business do you operate?")

            # Capture the state after the interaction
            await page.screenshot(path="/home/jules/verification/verification.png")
            print("Successfully verified the Streamlit application.")
        except Exception as e:
            print(f"An error occurred during verification: {e}")
            await page.screenshot(path="/home/jules/verification/error.png")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
