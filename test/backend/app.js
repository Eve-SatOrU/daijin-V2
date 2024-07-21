const express = require('express');

const app = express();
const port = 3000 || process.env.PORT;


const routes = require('./routes/router'); 
app.use('/', routes);

app.listen(port, () => { 
    console.log(`Vulnerable app listening at http://localhost:${port}`);
});