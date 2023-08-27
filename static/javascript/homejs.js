
const recentClothing = localStorage.getItem("currentClothing");

if (recentClothing) {
  const characterClothing = document.getElementById("character_clothing");
  characterClothing.src = recentClothing;
} else {
  const defaultClothing = "/procatstination/static/images/girl/girl/default_girl.png"; 
  const characterClothing = document.getElementById("character_clothing");
  characterClothing.src = defaultClothing;
}

const recentPet = localStorage.getItem("currentPet");

if (recentPet) {
  const characterPet = document.getElementById("character_pet");
  characterPet.src = recentPet;
} else {
  const defaultPet = "/procatstination/static/images/cats/cat/cat1.png"; 
  const characterPet = document.getElementById("character_pet");
  characterPet.src = defaultPet;
}
