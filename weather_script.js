// weather_script.js
// Función para obtener datos del clima desde la API de OpenWeatherMap
// Buenas prácticas: async/await, manejo de errores, parámetros configurables

/**
 * Obtiene los datos del clima para una ciudad usando la API de OpenWeatherMap.
 * @param {string} city - Nombre de la ciudad.
 * @param {string} apiKey - API Key de OpenWeatherMap.
 * @param {string} [units='metric'] - Unidades ('metric', 'imperial', 'standard').
 * @returns {Promise<Object>} - Datos del clima o error.
 */
async function getWeather(city, apiKey, units = 'metric') {
    const endpoint = `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(city)}&appid=${apiKey}&units=${units}`;
    try {
        const response = await fetch(endpoint);
        if (!response.ok) {
            throw new Error(`Error en la respuesta: ${response.status} ${response.statusText}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error al obtener los datos del clima:', error.message);
        throw error;
    }
}

// Ejemplo de uso:
// (async () => {
//     const apiKey = 'TU_API_KEY';
//     try {
//         const weather = await getWeather('Madrid', apiKey);
//         console.log(weather);
//     } catch (e) {
//         // Manejo de error
//     }
// })();

const readline = require('readline');
if (require.main === module) {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Introduce el nombre de la ciudad (por defecto: Santiago de Chile): ', (city) => {
        const selectedCity = city && city.trim() !== '' ? city : 'Santiago de Chile';
        rl.question('Introduce tu API Key de OpenWeatherMap: ', async (apiKey) => {
            try {
                const weather = await getWeather(selectedCity, apiKey);
                console.log('Datos del clima:', weather);
            } catch (e) {
                console.error('No se pudo obtener el clima.');
            } finally {
                rl.close();
            }
        });
    });
}

module.exports = { getWeather };
