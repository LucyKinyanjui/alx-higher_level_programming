$(function () {
  // Make an AJAX request to fetch data from the SWAPI API
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Update the text content of the <div id="character"> with the character name
    $('#character').text(data.name);
  });
});
