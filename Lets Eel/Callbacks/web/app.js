eel.expose(js_random);
// ######1
function js_random() {
  return Math.random();
}

// ####2##

// https://www.freecodecamp.org/news/javascript-callback-functions-what-are-callbacks-in-js-and-how-to-use-them/
// https://www.w3schools.com/js/js_callback.asp

eel.py_random()((n) => (document.getElementById("showRandom1").innerText = n));

eel.py_random()(function (n) {
  document.getElementById("showRandom2").innerText = n;
});

// let num = eel.py_random()(); //[object Promise]
// document.getElementById("showRandom1").innerText = num;

function updateTheHtml(n) {
  document.getElementById("showRandom3").innerText = n;
}
eel.py_random()(updateTheHtml); // no need to use async here
