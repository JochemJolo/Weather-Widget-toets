fetch("/weather")
    .then(response => response.json())
    .then(data => {
        console.log("City:", data.city);
        console.log("Temperature:", data.temperature + " °C");
        console.log("Weather:", data.weather);
        console.log("Time:", data.time);
    });