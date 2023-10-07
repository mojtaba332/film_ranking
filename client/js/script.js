const SERVER = 'localhost:5000';

function displayFilms(films){
    // Maak een lijstitem voor elke film en voeg deze toe aan de lijst       
    let container = document.querySelector('#filmsList tbody');
    container.innerHTML = '';
    for (const film of films) {
        const row = document.createElement('tr');
        row.innerHTML = '<td>'+ film.title + '</td>';
        container.appendChild(row);
    }
}

function displayFilmsRanking(films){
   // Maak een lijstitem voor elke film en voeg deze toe aan de lijst       
   let container = document.getElementById('rankingList');
   container.innerHTML = '';
   for (const film of films) {
       const listItem = document.createElement('li');
       listItem.textContent = `${film.title} - ${film.rank}`;
       container.appendChild(listItem);
   }
}

function getAndDisplayFilms(endPoint, displayFilms) {
    // Haal de lijst met films op van de backend API
    fetch(`http://${SERVER}/${endPoint}`)
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
    getAndDisplayFilms('films/ranking/5',displayFilmsRanking);
}

function clickedFilms(event){
    if (sectionFilms.classList.contains('active')) return;
    activateSection(sectionFilms);
    getAndDisplayFilms('films',displayFilms);
}


btnHome.onclick = clickedHome;
btnFilms.onclick = clickedFilms;
// btnUsers.onclick = clicked;
// btnAccount.onclick = clicked;

// Roep de functie aan om de lijst met films op te halen en weer te geven

clickedHome();
