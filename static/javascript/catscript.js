const recentPet = localStorage.getItem("currentPet");
    const characterPet = document.getElementById("character_pet");

    if (recentPet) {
      characterPet.src = recentPet;
    } else {
      characterPet.src = "/procatstination/static/images/cats/cat/cat1.png";
    }

function change_pet(pet) {
    const character_pet = document.getElementById("character_pet");
    character_pet.src = pet;
    localStorage.setItem("currentPet", pet);
}
  