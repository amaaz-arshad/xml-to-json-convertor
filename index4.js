const fs = require('fs').promises;
const xmljs = require('xml-js');

// Function to remove underscore prefix from keys
function removeUnderscorePrefix(obj) {
    if (Array.isArray(obj)) {
        return obj.map(removeUnderscorePrefix);
    } else if (typeof obj === 'object' && obj !== null) {
        return Object.entries(obj).reduce((acc, [key, value]) => {
            const newKey = key.startsWith('_') ? key.slice(1) : key;
            acc[newKey] = removeUnderscorePrefix(value);
            return acc;
        }, {});
    } else {
        return obj;
    }
}

async function main() {
    try {
        // Read all files in 'new-data' directory
        const files = await fs.readdir('new-data');
        
        // Filter to only XML files
        const xmlFiles = files.filter(file => file.endsWith('.xml'));

        // Initialize an array to hold the JSON objects
        const jsonArray = [];

        // Process each XML file
        for (const file of xmlFiles) {
            // Read the XML file
            const data = await fs.readFile(`new-data/${file}`, 'utf8');

            // Convert XML to JSON
            const json = xmljs.xml2js(data, { compact: true });

            // Remove underscore prefixes from keys
            const cleanedJson = removeUnderscorePrefix(json);

            // Add cleaned JSON object to the array
            jsonArray.push(cleanedJson);
        }

        // Convert the JSON array to a string with indentation
        const jsonString = JSON.stringify(jsonArray, null, 1);

        // Write the JSON string to a new file
        await fs.writeFile('new-json/data.json', jsonString);

        console.log('Successfully converted XML files to JSON and saved as data.json');

    } catch (err) {
        console.error('An error occurred:', err);
    }
}

main();
