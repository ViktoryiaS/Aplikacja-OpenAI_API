# Aplikacja do przetwarzania artykułów z OpenAI API   

## Krótki opis działania aplikacji:

Aplikacja przetwarza artykuł tekstowy, korzystając z API OpenAI, generując kod HTML, który zawiera odpowiednią strukturę artykułu, w tym obrazki, podpisy i tytuły.
1. Wczytanie artykułu: Aplikacja odczytuje artykuł z pliku tekstowego (artykuł.txt).
2. Przetwarzanie przez OpenAI: Artykuł jest przesyłany do OpenAI z odpowiednim promptem, który prosi o przekształcenie treści w strukturę HTML z użyciem odpowiednich tagów. Zawiera także instrukcję wstawiania obrazków z atrybutem alt oraz podpisów.
3. Zapis do pliku HTML: Wygenerowany przez OpenAI kod HTML jest zapisywany w pliku artykul.html.
4. Generowanie szablonu HTML: Tworzony jest pusty szablon HTML (szablon.html), który może być używany do wstawiania artykułów w przyszłości.
5. Podgląd artykułu: Pełny podgląd artykułu generowany jest w pliku podglad.html, który umożliwia wyświetlenie artykułu w przeglądarce internetowej.
   
Aplikacja umożliwia łatwą konwersję artykułów do formatu HTML, zachowując odpowiednią strukturę i oznaczenia dla obrazków.

## Krótkie wyjaśnienie kodu:

procesuj_artykul: Funkcja, która łączy się z API OpenAI, przetwarza artykuł i zwraca wygenerowany kod HTML.

wczytaj_artykuł: Wczytuje artykuł z pliku tekstowego.

zapisz_do_html: Zapisuje wygenerowany HTML do wskazanego pliku.

generuj_szablon_html: Tworzy pusty szablon HTML, w którym można umieścić artykuł.

generuj_podglad_html: Tworzy pełny podgląd HTML, w którym wstawiany jest wygenerowany artykuł.

Aplikacja zapisuje wygenerowane pliki HTML: artykul.html (z artykułem), szablon.html (pusty szablon) oraz podglad.html (pełny podgląd artykułu).

## Instrukcja użycia

Przygotowanie artykułu

Stwórz plik tekstowy (np. artykuł.txt) z artykułem, który chcesz przetworzyć. Plik powinien być zapisany w formacie tekstowym (np. .txt).

Ustawienie klucza API OpenAI
W kodzie, w miejscu openai.api_key = 'YOUR_OPENAI_API_KEY', wprowadź swój klucz API OpenAI.

Klucz API możesz uzyskać, rejestrując się na stronie OpenAI.

## Uruchomienie skryptu

### Uruchamianie skryptu w IDLE (Python 3.12.4):

#### 1. Pobierz lub sklonuj repozytorium:
   
Otwórz repozytorium w przeglądarce: ``` github.com ```
   
Opcja 1: Pobierz plik ZIP z repozytorium z GitHub i wypakuj go na swoim komputerze.

Opcja 2: Skorzystaj z Git i sklonuj repozytorium:

``` git clone https://github.com/ViktoryiaS/Aplikacja-OpenAI_API.git ```

#### 2. Otwórz IDLE:

Windows: Wyszukaj "IDLE" w menu Start.

Mac/Linux: Uruchom idle3 z terminala.

#### 3. Otwórz skrypt:

W IDLE kliknij File > Open i wybierz swój skrypt (np. app.py).

#### 4. Uruchom skrypt:

Kliknij Run > Run Module lub naciśnij F5.

#### Skrypt wykonuje następujące kroki:

Wczytuje zawartość pliku tekstowego artykuł.txt.

Wysyła artykuł do API OpenAI w celu obróbki.

Zapisuje wynikowy kod HTML w pliku artykul.html.

Dodatkowo, generuje szablon HTML w pliku szablon.html oraz pełny podgląd artykułu w pliku podglad.html.

#### Sprawdzenie wyników:

Pliki wynikowe (artykul.html, szablon.html, podglad.html) pojawią się w folderze, w którym uruchomiłeś skrypt.

### Alternatywnie, aby uruchomić skrypt z terminala: 

W terminalu wpisz:

python app.py


Skrypt wczyta zawartość pliku tekstowego artykuł.txt, wyśle go do API OpenAI w celu obróbki, a następnie zapisze wynikowy kod HTML w pliku artykul.html.
Dodatkowo, wygeneruje szablon HTML (szablon.html) oraz pełny podgląd artykułu w pliku podglad.html.


## Wygenerowane pliki:

Po uruchomieniu skryptu w folderze roboczym pojawią się trzy pliki:

artykul.html – plik zawierający kod HTML wygenerowany przez OpenAI, który zawiera artykuł w odpowiednich tagach HTML.

szablon.html – pusty szablon HTML, który może być używany do późniejszego generowania podglądów artykułów. Sekcja <body> powinna być pusta, gotowa do wklejenia artykułu.

podglad.html – plik zawierający pełny podgląd artykułu, który zawiera zarówno szablon HTML, jak i artykuł wstawiony do sekcji <body>.

### Wykorzystanie wygenerowanego HTML:

Możesz otworzyć pliki szablon.html oraz podglad.html w dowolnej przeglądarce, aby zobaczyć wygenerowany artykuł w formacie HTML.

# Szczegóły implementacji
## Struktura projektu:

W projekcie znajdują się następujące pliki:

app.py: Główny skrypt odpowiedzialny za łączenie z API OpenAI, przetwarzanie artykułu, generowanie HTML oraz zapisywanie wyników do plików.

artykuł.txt: Plik zawierający artykuł do przetworzenia (zastąp tym plikiem swój własny artykuł).

szablon.html: Pusty szablon HTML, który może być używany do późniejszego generowania podglądów artykułów.

podglad.html: Plik zawierający pełny podgląd artykułu w formacie HTML.

## Działanie skryptu:

Skrypt wczytuje artykuł z pliku artykuł.txt.
Następnie, artykuł jest przetwarzany przez OpenAI przy użyciu odpowiedniego promptu.
Wygenerowany HTML jest zapisany w pliku artykul.html.
Tworzony jest także szablon HTML (szablon.html) oraz podgląd artykułu (podglad.html).

## Kod skryptu

W załączeniu znajduje się kod, który wykonuje wszystkie operacje wymagane w projekcie:

```
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
    5. Brak CSS i JavaScript i tylko zawartość do wstawienia pomiędzy tagami <body> i </body>..
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

 ```

Po wykonaniu tych kroków, Twoja aplikacja będzie gotowa do przetwarzania artykułów i generowania kodu HTML!




