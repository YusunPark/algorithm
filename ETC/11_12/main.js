var input = document.getElementsByClassName('SearchInput__input')[0];
var suggetion = document.getElementsByClassName('Suggestion')[0];
var selectedLanguage = document.getElementsByClassName('SelectedLanguage')[0];
suggetion.style.display = 'none';

var ul_lang = document.createElement('ul');
selectedLanguage.appendChild(ul_lang);

var ul = document.createElement('ul');
suggetion.appendChild(ul);
var select = 0;

const changeInput = (e) => {
  var query;
  e.target.value ? (query = e.target.value) : (query = null);
  fetch(`https://wr4a6p937i.execute-api.ap-northeast-2.amazonaws.com/dev/languages?keyword=${query}`)
    .then((res) => {
      return res.json();
    })
    .then((data) => {
      console.log(data);
      if (data.length == 0) {
        suggetion.style.display = 'none';
        return;
      }
      data.map((v, i) => {
        suggetion.style.display = 'block';
        if (ul.childElementCount > i) {
          var li = ul.childNodes[i];
          const words = v.split(`${e.target.value}`);
          li.innerHTML = `${words[0] ? words[0] : null}<span class="Suggestion__item--matched">${
            e.target.value
          }</span>${words[1] ? words[1] : null}`;
        } else {
          const words = v.split(`${e.target.value}`);
          var li = document.createElement('li');
          li.innerHTML = `${words[0] ? words[0] : null}<span class="Suggestion__item--matched">${
            e.target.value
          }</span>${words[1] ? words[1] : null}`;
          ul.appendChild(li);
        }
      });
      ul.childNodes[select].className = 'Suggestion__item--selected';

      ul.childNodes.forEach((el) => {
        el.addEventListener('click', (event) => {
          var li_lang = document.createElement('li');
          li_lang.innerHTML = event.target.textContent;
          ul_lang.appendChild(li_lang);
          if (ul_lang.childElementCount > 5) {
            ul_lang.removeChild(ul_lang.firstChild);
          }
        });
      });
    });
};

addEventListener('input', (e) => {
  changeInput(e);
});

input.addEventListener('keydown', (e) => {
  if (e.keyCode === 13) {
    alert(ul.childNodes[select].textContent);
  } else if (e.keyCode == 38) {
    ul.childNodes[select].className = '';
    select = (ul.childElementCount + select - 1) % ul.childElementCount;
    ul.childNodes[select].className = 'Suggestion__item--selected';
  } else if (e.keyCode == 40) {
    ul.childNodes[select].className = '';
    select = (select + 1) % ul.childElementCount;
    ul.childNodes[select].className = 'Suggestion__item--selected';
  }
});
