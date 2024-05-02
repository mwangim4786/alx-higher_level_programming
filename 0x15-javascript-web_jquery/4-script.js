const header = $('header');

$('DIV#toggle_header').click(() => {
  header.toggleClass('red');
  header.toggleClass('green');
});
