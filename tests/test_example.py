import re 
from playwright.sync_api import Page, expect #importando o playwright api e usando-o como "re", por algum motivo não pode na mesma linha

def test_has_title(page: Page):
    # Navega para a página do Playwright (ou qualquer outra url que eu colocar)
    page.goto("https://playwright.dev/")

    #Uma espécie de if que serve para verificar se o titulo da página (to_have_title) realmente contem a palavra que eu escrever ("Playwright"), assim da pra confirmar que o teste funcionou.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    page.get_by_role("link", name="Get started").click()

    expect(page.get_by_role("heading", name="Installation")).to_be_visible()