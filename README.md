# Aplikacja do przetwarzania artykułów z OpenAI API                                                            Krótki opis działania aplikacji:
Aplikacja przetwarza artykuł tekstowy, korzystając z API OpenAI, generując kod HTML, który zawiera odpowiednią strukturę artykułu, w tym obrazki, podpisy i tytuły.
1. Wczytanie artykułu: Aplikacja odczytuje artykuł z pliku tekstowego (artykuł.txt).
2. Przetwarzanie przez OpenAI: Artykuł jest przesyłany do OpenAI z odpowiednim promptem, który prosi o przekształcenie treści w strukturę HTML z użyciem odpowiednich tagów, takich jak <h1>, <p>, <img>, itd. Zawiera także instrukcję wstawiania obrazków z atrybutem alt oraz podpisów.
3. Zapis do pliku HTML: Wygenerowany przez OpenAI kod HTML jest zapisywany w pliku artykul.html.
4. Generowanie szablonu HTML: Tworzony jest pusty szablon HTML (szablon.html), który może być używany do wstawiania artykułów w przyszłości.
5. Podgląd artykułu: Pełny podgląd artykułu generowany jest w pliku podglad.html, który umożliwia wyświetlenie artykułu w przeglądarce internetowej.
Aplikacja umożliwia łatwą konwersję artykułów do formatu HTML, zachowując odpowiednią strukturę i oznaczenia dla obrazków.


