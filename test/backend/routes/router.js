const express = require('express');
// router express
const router = express.Router();
const controller=require("../controllers/controller");

router.get('/', controller.index);
router.get('/lfi', controller.getlfi);


module.exports =router;