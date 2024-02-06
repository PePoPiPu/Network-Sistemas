let lista_activas = []
console.log(lista_activas)
let lista_inactivas = []
fetch('ips_activas.json')
.then(response => response.json())
.then(data => {
    console.log('Fetched active IPs:', data);
    if (data && data.activas) {
        // Populate the lista_activas array
        lista_activas = data.activas.map(ipObj => ipObj.activa);

        // You can use the populated array elsewhere in your script
        console.log('Populated lista_activas array:', lista_activas);
    } else {
        console.error('Invalid or missing data in ips_activas.json');
    }
})
.catch(error => console.error('Error fetching active IPs:', error));

function fActivas() {
    let html = "<table>"
    for (i = 0; i < lista_activas.length; i++) {
        html += "<tr>"
        html += "<td>" + lista_activas[i] + "</td>"
        html += "</tr>"
    }
    html += "</table>"
    document.querySelector("section").innerHTML = html;
}