const menu = document.getElementById('menu')
console.log(menu)

function toggleMenu(){
    if (menu.classList.contains("closed") == true){
        menu.classList.remove("closed")
        console.log('teste')
    } else{
        menu.classList.add("closed")
    }

}