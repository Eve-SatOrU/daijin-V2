const fs = require('fs');
const path = require('path');


// i will add front end later
exports.index =(req, res) => {
    res.send(`
        <p>Use the links below to test  >< :</p>
        <ul>
        </ul>
    `);
};


exports.getlfi =(req, res) => { 
    const file = req.query.file || './util/test.json'  ;
    try {
        const data = fs.readFileSync(file, 'utf8'); 
        res.send(data);
    } catch (err) {
        res.send(`Error reading file: ${err.message}`);
    }
};