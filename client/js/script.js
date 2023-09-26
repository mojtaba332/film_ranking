
function displayFilms(films){
     // Sorteer de films op basis van hun titel
    films.sort((a, b) => b.title < a.title);
    // Maak een lijstitem voor elke film en voeg deze toe aan de lijst       
    let container = document.querySelector('#filmsList tbody');
    container.innerHTML = '';
    for (const film of films) {
        const row = document.createElement('tr');
        row.innerHTML = '<td>'+ film.title + '</td>';
        container.appendChild(row);
    }
}

function displayFilmsRanked(films){
    // Sorteer de films op basis van hun ranking
   films.sort((a, b) => b.rank - a.rank);
   // Maak een lijstitem voor elke film en voeg deze toe aan de lijst       
   let container = document.getElementById('rankingList');
   container.innerHTML = '';
   for (const film of films) {
       const listItem = document.createElement('li');
       listItem.textContent = `${film.title} - ${film.rank}`;
       container.appendChild(listItem);
   }
}

function getAndDisplayFilms(displayFilms) {
    // Haal de lijst met films op van de backend API
    fetch('http://localhost:5000/films')
        .then(response => response.json())
        .then(films => {
            displayFilms(films);
        });
}

function activateSection(section){  
    let sections = document.querySelectorAll('section');
    sections.forEach((section)=>{section.classList.remove('active')});
    section.classList.add('active');
}

function clickedHome(event){
    if (sectionHome.classList.contains('active')) return;
    activateSection(sectionHome);
    getAndDisplayFilms(displayFilmsRanked);
}

function clickedFilms(event){
    if (sectionFilms.classList.contains('active')) return;
    activateSection(sectionFilms);
    getAndDisplayFilms(displayFilms);
}


btnHome.onclick = clickedHome;
btnFilms.onclick = clickedFilms;
// btnUsers.onclick = clicked;
// btnAccount.onclick = clicked;

// Roep de functie aan om de lijst met films op te halen en weer te geven

clickedHome();
