var string = "Welcome to millo!";
var str = string.split("");
var el = document.getElementById('str');
(function animate() {
  str.length > 0 ? el.innerHTML += str.shift() : clearTimeout(running);
  var running = setTimeout(animate, 90);
})();
