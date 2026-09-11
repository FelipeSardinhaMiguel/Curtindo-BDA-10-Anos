from playwright.sync_api import Page, BrowserContext, expect

def test_github_auth(browser):

    #criando um novo contexto de navegador
    #context = browser.new_context()
    context = browser.new_context(storage_state="auth.json")

    #criando uma nova página no contexto que eu criei
    page = context.new_page()

    page.goto("https://github.com/")

    #Para o navegador não fechar sozinho enquanto eu estiver testando.
    #page.pause()

    #para criar o auth.json, onde será armazenado as minhas credenciais de login.
    #context.storage_state(path="auth.json")

    #Para confirmar que o login foi feito com sucesso.
    page.get_by_role("button", name="Open user navigation menu").click()

    #espera com que o botão fique visivel antes de terminar o código para a verificação.
    expect(page.get_by_role("link", name="Sign out")).to_be_visible()