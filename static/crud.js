
let total = 0;
let displayTotal = document.getElementById("total-value");

if (displayTotal) {
    displayTotal.innerHTML = total;
} else {
    console.error("Element with id 'total-value' not found!");
}

const buy = (id) => {
    console.log(`Buying ${id}`);
    axios.post(`http://127.0.0.1:5000/add`, { id })


}
const remove = (id) => {
    console.log(`removing ${id}`);
    axios.delete(`http://127.0.0.1:5000/delete/${id}`)
}