const fs = require("fs");
const xml2js = require("xml-js");

// Read the XML file
fs.readFile("books.xml", "utf8", (err, data) => {
  if (err) {
    console.error("Failed to read XML file:", err);
    return;
  }

  // Convert XML to JSON
  const json = xml2js.xml2json(data, { spaces: 2 });

  // Write the JSON string to a new file
  fs.writeFile("books2.json", json, (err) => {
    if (err) {
      console.error("Failed to write JSON file:", err);
      return;
    }

    console.log("Successfully converted XML to JSON and saved as books.json");
  });
});
