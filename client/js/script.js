function getAndDisplayFilms() {
    // Haal de lijst met films op van de backend API
    fetch('http://localhost:5000/films')
        .then(response => response.json())
        .then(films => {
            console.log(films)
            // Sorteer de films op basis van hun ranking
            films.sort((a, b) => b.rank - a.rank);
            console.log(films);

            // Maak een lijstitem voor elke film en voeg deze toe aan de lijst
            for (const film of films) {
                const listItem = document.createElement('li');
                console.dir(film);
                listItem.textContent = `${film.title} - ${film.rank}`;
                filmList.appendChild(listItem);
            }
        });
}

// Roep de functie aan om de lijst met films op te halen en weer te geven
getAndDisplayFilms();

