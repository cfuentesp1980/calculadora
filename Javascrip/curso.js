const h1 = document.querySelector('h1');
const p = document.querySelector('p');
const parrafito = document.querySelector('.parrafito');
const pid = document.querySelector('#pid');
const input = document.querySelector('input');



console.log({
    h1,
    p,
    parrafito,
    pid,
    input,
});

/*h1.innerText = 'Patito <br> Feo';
h1.innerHTML = 'Patito <br> Feo';*/

const img = document.createElement('img');
img.setAttribute('src','https://static.platzi.com/static/images/conf/logo_black@2x.png');
console.log(img);

pid.append(img);

console.log(input.value);