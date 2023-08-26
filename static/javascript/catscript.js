const recentCat = localStorage.getItem("currentCat");
    const cat_clothing = document.getElementById("cat_clothing");

    if (recentCat) {
        cat_clothing.src = recentCat;
    } else {
        cat_clothing.src = "/procatstination/static/images/cats/cat/cat1.png";
    }

function change_cat(cat) {
    const cat_clothing = document.getElementById("cat_clothing");
    cat_clothing.src = cat;
    localStorage.setItem("currentCat", cat);
}
  