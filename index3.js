const fs = require('fs');
const xml2js = require('xml-js');

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

// Read the XML file
fs.readFile('new-data/00_Vorwort_647cafc6-0bc7-4ee0-9596-59ee231be92f.xml', 'utf8', (err, data) => {
    if (err) {
        console.error('Failed to read XML file:', err);
        return;
    }

    // Convert XML to JSON
    const json = xml2js.xml2js(data, { compact: true });

    // Remove underscore prefixes from keys
    const cleanedJson = removeUnderscorePrefix(json);

    // Convert cleaned JSON to string with indentation
    const jsonString = JSON.stringify(cleanedJson, null, 1);

    // Write the JSON string to a new file
    fs.writeFile('new-json/NBesG.json', jsonString, (err) => {
        if (err) {
            console.error('Failed to write JSON file:', err);
            return;
        }

        console.log('Successfully converted XML to JSON and saved as books.json');
    });
});
