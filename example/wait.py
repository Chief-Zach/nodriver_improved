import nodriver_improved as uc

async def main():
    browser = await uc.start()
    page = await browser.get("http://127.0.0.1:8000/wait.html")
    text = await page.timed_query_selector_all("div[class='content']")
    text = await page.find("div[class='content']")
    print([x.text_all for x in text])




if __name__ == '__main__':
    uc.loop().run_until_complete(main())
