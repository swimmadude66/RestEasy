var express = require('express');
var rest = require('restler');
var crypto = require('crypto');
var router = express.Router();


router.get('/api/pins/:id', function(req, res) {
    var pin_id  = req.params.id;
    child_process.exec('python  /opt/RestEasy/get_pin.py ' + pin_id.toString(), function(err, stdout, stderr){
            if(err){
                console.log(err);
                return res.send({success: false, error: err});
            }
            else{
                var result = JSON.parse(stdout);
                return res.send(result);
            }
    });
});


router.post('/api/pins/:id', function(req, res) {
    //create the user here
    h = req.headers;
});

module.exports = router;
