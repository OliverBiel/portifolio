const menuElement = document.getElementById('menu')
const menuContent = document.getElementById('menu-content')
const iconHeader = document.querySelector('#menu-btn i')

function toggleMenu(){
    if (menuElement.classList.contains("closed") === true){
        menuElement.classList.remove("closed")
    } else{
        menuElement.classList.add("closed")
    }
}

function func(e){
    if (((e.target != menuContent) & (menuElement.classList.contains("closed") === false)) & e.target != iconHeader){
        toggleMenu()
    }
}