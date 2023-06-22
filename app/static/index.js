// async function getapi(city) {
//     const app_id = '7984d743b5094cd6e05a6650b8585015';
//     const res = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${app_id}&units=metric`, 
//     {
//         method: 'GET',
//     })
//     .then((response) => response.json())
//     .then((data) => {
//         console.log("Success:", data);
//         })
//         .catch((error) => {
//         console.error("Error:", error);
//     })};

// function displayData(data) {
//     const outputDiv = document.getElementById('weather-results')
//     const outputCity = city;
//     const outputTemp = data.main.temp;
//     const outputDesc = data.weather.description
//     const outputIcon = data.weather.icon
//     let html = '';
//     for (const item of data) {
//       html += `<div>${item.name}: ${item.value}</div>`;
//     }
//     outputDiv.innerHTML = html;
//   }

// async function geticon(icon) {
//     fetch(`https://openweathermap.org/img/wn/${icon}@2x.png`, {
//         method: 'GET',
//     }).then(response => {
//     if(response.ok) {
//         return response.json();
//     } else {
//         throw new Error('Error');
//     }})
//     .them(data => {
//         displayPhoto(data);
//     })
//     .catch(error => {
//         console.error('Error fetching data:', error)
//     });
//     }