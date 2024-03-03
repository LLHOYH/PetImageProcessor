const fs = require("fs");
const path = require("path");

async function call() {
  // Read the image file asynchronously

  const dirPath = "images/";
  const files = fs.readdirSync(dirPath);

  var postID=0, userID=0, category='spotted', phone="61468431079";

  var postInfos=[]
  for(let i=0; i<files.length;i++){
    
    const filePath = path.join(dirPath, files[i]);
    const imageData = fs.readFileSync(filePath);

    postID++;
    userID++;

    const lng = (Math.random() * 360) - 180; // Range: -180 to 180
    const lat = (Math.random() * 180) - 90;  // Range: -90 to 90
    let place =  { lng, lat };

    console.log(imageData)
    let header = {
      method: "POST",
      headers: { "Content-Type": " text/plain" },
      body: imageData,
    };

    let result = await fetch(
      "https://zr1hmbzyc2.execute-api.ap-southeast-1.amazonaws.com/dev/api/uploadPost",
      header
    );
    let data = await result.json();
    console.log(data)

    postInfos.push({
        postID,
        userID,
        category,
        phone,
        dateTime:new Date(),
        place:JSON.stringify(place),
        image:data
    })

  }

  const jsonData = JSON.stringify(postInfos);
  const jsonFilePath = 'data.json';
  fs.writeFile(jsonFilePath, jsonData, (err) => {
    if (err) {
      console.error('Error writing to file:', err);
      return;
    }
    console.log('Data has been written to', jsonFilePath);
  });

  // csvGenerator(postInfos)
}


async function csvGenerator(data){
    const { createObjectCsvWriter } = require('csv-writer');

// Define CSV header
const csvHeader = [
    { id: 'postID', title: 'postID' },
    { id: 'userID', title: 'userID' },
    { id: 'category', title: 'category' },
    { id: 'place', title: 'place' },
    { id: 'phone', title: 'phone' },
    { id: 'image', title: 'image' }
];

// Create CSV writer
const csvWriter = createObjectCsvWriter({
    path: 'output_test.csv',
    header: csvHeader
});

// Write data to CSV file
csvWriter.writeRecords(data)
    .then(() => console.log('CSV file written successfully'))
    .catch((err) => console.error('Error writing CSV file:', err));

}

call();
