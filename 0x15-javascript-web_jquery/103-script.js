$(function () {
  function fetchTranslation () {
    const languageCode = $('#language_code').val();

    // Make the API request
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      type: 'GET',
      data: { lang: languageCode },
      success: function (response) {
        // Display the translation in the DIV#hello element
        $('#hello').text(response.hello);
      },
      error: function (error) {
        console.log('Error:', error);
      }
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      // If ENTER key is pressed, fetch translation
      fetchTranslation();
    }
  });
});
