const cols = document.getElementsByClassName('id-column');

for (let i = 0; i < cols.length; i++) {
  cols[i].addEventListener('click', () => {
    const getUrl = window.location;
    window.location = cols[i].attributes['data-url'].value + '/' + cols[i].innerHTML;
  });
}
