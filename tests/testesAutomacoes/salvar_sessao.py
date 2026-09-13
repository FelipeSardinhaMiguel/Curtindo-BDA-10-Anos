from playwright.sync_api import sync_playwright

def criar_sessao_autenticada():
    with sync_playwright() as p:
        # esse args serve para evitar que o YouTube detecte que é um navegador automatizado.
        browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        
        context = browser.new_context()
        page = context.new_page()

        print("Redirecionando para o login do Google/YouTube...")
        page.goto("https://accounts.google.com/")

        print("\n--- AÇÃO REQUERIDA ---")
        print("1. Faça o login manualmente na janela do navegador que se abriu.")
        print("2. Após concluir o login e estar no YouTube/Google, volte aqui no terminal.")
        input("3. Pressione ENTER neste terminal para salvar a sessão...")

        # Salva os cookies e a sessão no arquivo JSON
        context.storage_state(path="auth/youtube.json")
        print("Sessão salva com sucesso em 'auth/youtube.json'!")
        
        browser.close()

if __name__ == "__main__":
    criar_sessao_autenticada()