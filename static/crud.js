
let total = 0;
let displayTotal = document.getElementById("total-value");

if (displayTotal) {
    displayTotal.innerHTML = total; 
} else {
    console.error("Element with id 'total-value' not found!");
}

const add = (id) =>{
    console.log(`Adding ${id}`);
    
}
