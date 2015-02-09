var express = require('express');
var rest = require('restler');
var crypto = require('crypto');
var childProcess = require('child_process');
var router = express.Router();


router.get('/api/pins/', function(req, res) {
    childProcess.exec('python  /opt/RestEasy/python/get_pin.py -a', function(err, stdout, stderr){
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

router.get('/api/pins/:id', function(req, res) {
    var pin_id  = req.params.id;
    childProcess.exec('python  /opt/RestEasy/python/get_pin.py ' + pin_id.toString(), function(err, stdout, stderr){
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


router.post('/api/pins/', function(req, res) {
    b = req.body;

    childProcess.exec('python  /opt/RestEasy/python/set_pin.py \'' + JSON.stringify(b)+'\'', function(err, stdout, stderr){
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

module.exports = router;
