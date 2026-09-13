#importando o playwright api e usando-o como "re", por algum motivo não pode na mesma linha
import re #isso é do python.
from playwright.sync_api import Page, expect, BrowserContext #isso é do playwright.

def test_youtube(browser):
    context = browser.new_context(storage_state="auth/youtube.json") #A autenticação do youtube.json está no outro arquivo(salvar_sessao.py).

    page = context.new_page()

    page.goto("https://www.youtube.com/")


    expect(page).to_have_title(re.compile("YouTube"))

    #Procurando a caixa de pesquisa pelo placeholder.
    page.get_by_placeholder("Pesquisar").fill("BDA 10 anos")
    page.get_by_placeholder("Pesquisar").press("Enter")

    #print(page.url)
    #1ª verificação de que a pesquisa funcionou (pela pesquisa no input).
    expect(page.get_by_placeholder("Pesquisar")).to_have_value("BDA 10 anos")

    #2ª verificação de que a pesquisa funcionou (pela URL).
    expect(page).to_have_url(re.compile("search_query=BDA\\+10\\+anos"))

    page.get_by_text("Batalha da Aldeia - Especial 10 anos").first.click()

    page.get_by_role("button", name=re.compile("Gostei", re.IGNORECASE)).first.click()

    #tentar mutar o video quando ele começar.
    page.locator(".ytp-mute-button").click()