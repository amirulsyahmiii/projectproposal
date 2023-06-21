setInterval(function() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('mqtt-data').innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "{% url 'mqtt_handler' %}", true);
    xhttp.send();
}, 1000);
