const menuElement = document.getElementById('menu')
console.log(menuElement)

function toggleMenu(){
    if (menuElement.classList.contains("closed") === true){
        menuElement.classList.remove("closed")
    } else{
        menuElement.classList.add("closed")
    }
}