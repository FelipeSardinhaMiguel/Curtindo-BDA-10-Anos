#importando o playwright api e usando-o como "re", por algum motivo não pode na mesma linha
import re #isso é do python.
from playwright.sync_api import Page, expect #isso é do playwright.

def test_youtube(page: Page):
    page.goto("https://www.youtube.com/")

    expect(page).to_have_title(re.compile("YouTube"))

    #Procurando a caixa de pesquisa pelo placeholder.
    page.get_by_placeholder("Pesquisar").fill("BDA 10 anos")
    page.get_by_placeholder("Pesquisar").press("Enter")

    #1ª verificação de que a pesquisa funcionou (pela pesquisa no input).
    expect(page.get_by_placeholder("Pesquisar")).to_have_value("BDA 10 anos")
    #2ª verificação de que a pesquisa funcionou (pela URL).
    expect(page).to_have_url(re.compile("search_query=BDA+10+anos"))

