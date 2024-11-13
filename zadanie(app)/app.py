import openai
import os

# Ustawienie klucza API OpenAI
openai.api_key = 'Tutaj musi być klucz API'

# Funkcja do łączenia się z OpenAI API i przetwarzania artykułu
def procesuj_artykul(artykul_text, prompt):
    # Użycie modelu ChatGPT do przetworzenia artykułu
    response = openai.ChatCompletion.create(
        model="gpt-4",  
        messages=[
            {"role": "system", "content": "Jesteś asystentem, który pomaga w przetwarzaniu artykułów."},
            {"role": "user", "content": f"{prompt}\n\nArtykuł:\n{artykul_text}"}
        ],
        max_tokens=2000,
        temperature=0.7
    )
    
    return response['choices'][0]['message']['content'].strip()

# Funkcja do wczytania artykułu z pliku
def wczytaj_artykuł(plik):
    with open(plik, 'r', encoding='utf-8') as file:
        return file.read()

# Funkcja do zapisu wyniku do pliku HTML
def zapisz_do_html(wynik, plik_output):
    with open(plik_output, 'w', encoding='utf-8') as file:
        file.write(wynik)

# Funkcja do generowania pustego szablonu HTML
def generuj_szablon_html():
    szablon = """
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Podgląd Artykułu</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
            }
            h1, h2, p {
                margin-bottom: 15px;
            }
            img {
                max-width: 100%;
                height: auto;
            }
        </style>
    </head>
    <body>
        <!-- artykuł -->
    </body>
    </html>
    """
    return szablon

# Funkcja do generowania pełnego podglądu artykułu
def generuj_podglad_html(artykul_html):
    podglad = f"""
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Podgląd Artykułu</title>
        <style>
            body {{
                color: green;
                background-color: #f4f4f9;
                font-family: Arial, sans-serif;
                margin: 20px;
            }}
            h1, h2 {{
                color: blue;
                margin-bottom: 15px;
            }}
            p{{
               color: pink;
              line-height: 1.6;
              margin: 10px 0;
              }}
            img {{
                max-width: 100%;
                height: auto;
            }}
        </style>
    </head>
    <body>
        {artykul_html} <!-- Tutaj wstawiamy przetworzony artykuł -->
    </body>
    </html>
    """
    return podglad

# Główna funkcja, która łączy wszystko razem
def main():
    # Ścieżka do pliku tekstowego z artykułem
    artykul_plik = 'artykuł.txt'  
    
    # Wczytanie treści artykułu
    artykul_text = wczytaj_artykuł(artykul_plik)
    
    # Prompt dla OpenAI
    prompt = """
    Zmien ten artykuł w kod HTML, który:
    1. Używa odpowiednich tagów HTML do strukturyzacji treści, takich jak <h1>, <h2>, <p>, <ul>, <li> itp.
    2. Wstawia tagi <img> w miejscach, które mogą wymagać ilustracji z atrybutem 'src' wskazującym na 'image_placeholder.jpg'.
    3. Dodaje atrybut 'alt' do każdego obrazka z dokładnym promptem, który możemy użyć do wygenerowania grafiki.
    4. Dodaje podpisy pod grafikami używając tagu <figcaption>.
    5. Brak CSS i JavaScript i tylko zawartość do wstawienia pomiędzy tagami <body> i </body>..
    """
    
    # Procesowanie artykułu przez OpenAI
    wynik_html = procesuj_artykul(artykul_text, prompt)
    
    # tutaj chodzi o to, ze wynik zapisuję się do pliku html 
    zapisz_do_html(wynik_html, 'artykul.html')
    
    print("Artykuł został przetworzony i zapisany do 'artykul.html'.")

    # Generowanie pustego szablonu HTML
    szablon_html = generuj_szablon_html()
    zapisz_do_html(szablon_html, 'szablon.html')

    # Generowanie pełnego podglądu artykułu
    podglad_html = generuj_podglad_html(wynik_html)
    zapisz_do_html(podglad_html, 'podglad.html')

    print("Szablon i podgląd artykułu zostały zapisane do 'szablon.html' i 'podglad.html'.")

# Uruchomienie aplikacji
if __name__ == "__main__":
    main()
