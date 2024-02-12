let lista_activas = []
console.log(lista_activas)
let lista_binarias = []

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




window.onbeforeunload = function () {
    window.scrollTo(0, 0);
}

function fActivas() {
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: "smooth"
    });
    let html = "<table id='tabla1'>";
    for (i = 0; i < lista_activas.length; i++) {
        html += "<tr>";
        html += "<td>" + lista_activas[i] + "</td>";
        html += "</tr>";
    }
    html += "</table>"
    document.querySelector("#activas").innerHTML = html;
}

function fBinarias() {
    document.querySelector("#loader").style.visibility = "visible";
    document.querySelector("#loader_texto").style.visibility = "visible";
    fetch('ips_binarias.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const items = data.ip_binaria;

            const shuffledItems = items.sort(() => Math.random() - 0.5);
            const randomItems = shuffledItems.slice(0, 5);
            const lista_binarias = randomItems.map(item => item.ip_binaria);
            document.querySelector("#loader").style.visibility = "hidden";
            document.querySelector("#loader_texto").style.visibility = "hidden";
            window.scrollTo({
                top: document.body.scrollHeight,
                behavior: "smooth"
            });
            // Generate HTML table
            let html = "<table>";
            lista_binarias.forEach(ip => {
                html += "<tr>";
                html += "<td>" + ip + "</td>";
                html += "</tr>";
            });
            html += "</table>";
            document.querySelector("#binarias").innerHTML = html;
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}

function fVerCaptura() {
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: "smooth"
    });
}