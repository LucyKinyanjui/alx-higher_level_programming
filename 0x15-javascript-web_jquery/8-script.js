$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    const listMovies = $('#list_movies');

    // Loop through each movie and append its title to the list
    $.each(movies, function (index, movie) {
      const listItem = $('<li>').text(movie.title);
      listMovies.append(listItem);
    });
  });
});
