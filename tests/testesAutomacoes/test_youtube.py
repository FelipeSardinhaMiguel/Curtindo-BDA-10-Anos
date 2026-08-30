#importando o playwright api e usando-o como "re", por algum motivo não pode na mesma linha
import re #isso é do python.
from playwright.sync_api import Page, expect #isso é do playwright.

def test_youtube(page: Page):
    page.goto("https://www.youtube.com/")

    expect(page).to_have_title(re.compile("youtube"))


