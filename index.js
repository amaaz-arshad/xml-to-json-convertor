const fs = require("fs");
const xml2js = require("xml2js");

// Create an instance of the xml2js parser
const parser = new xml2js.Parser();

// Read the XML file
fs.readFile("NBesG.xml", (err, data) => {
  if (err) {
    console.error("Failed to read XML file:", err);
    return;
  }

  // Parse the XML to JSON
  parser.parseString(data, (err, result) => {
    if (err) {
      console.error("Failed to parse XML:", err);
      return;
    }

    // Convert the result JSON to string
    const json = JSON.stringify(result, null, 0.25);

    // Write the JSON string to a new file
    fs.writeFile("NBesG1.json", json, (err) => {
      if (err) {
        console.error("Failed to write JSON file:", err);
        return;
      }

      console.log("Successfully converted XML to JSON and saved as books.json");
    });
  });
});
