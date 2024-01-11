$(function () {
  // Make an AJAX request to fetch data from the specified URL
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Update the text content of the <div id="hello"> with the fetched translation
    $('#hello').text(data.hello);
  });
});
