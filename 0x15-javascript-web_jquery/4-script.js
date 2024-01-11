$(function () {
  // Add a click event listener to the element with id "toggle_header"
  $('#toggle_header').click(function () {
    // Select the <header> element
    const header = $('header');

    // Toggle between the classes "red" and "green"
    if (header.hasClass('red')) {
      header.removeClass('red').addClass('green');
    } else {
      header.removeClass('green').addClass('red');
    }
  });
});
