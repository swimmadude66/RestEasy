var express = require('express');
var rest = require('restler');
var crypto = require('crypto');
var router = express.Router();
var fs = require("fs");
var file = "/opt/RestEasy/RestEasy.db";
var exists = fs.existsSync(file);
var sqlite3 = require("sqlite3").verbose();
var db = new sqlite3.Database(file);


function rand(rlen){
    var text = "";
    var possible = "ABCDEFabcdef0123456789";
    for( var i=0; i < rlen; i++ )
        text += possible.charAt(Math.floor(Math.random() * possible.length));
    return text;
}

router.post('/api/users/', function(req, res) {
            //create the user here
	    h = req.headers;
	    var uname = h.uname.toString();
	    var pass = h.pass.toString();
	    if(uname == null || pass.length < 6){
		console.log('Bad Username or pass');
	    	return res.send( {error: 'Username or password do not meet requirements' });
    	    }
            console.log('Creating User');
	    var shasum = crypto.createHash('sha256');
	    var unamesha = crypto.createHash('sha256');
	    unamesha.update(uname);
            var salt = unamesha.digest('hex');
	    console.log('Salt = ' + salt);
	    shasum.update(salt + pass);
	    db.run("Insert Into Users (username, pass_hash, isAdmin, isActive) Values(?, ?, 0, 1 )", uname, shasum.digest('hex'), function(err){
		if(err){
		    console.log(err);
   		    return res.send({success: false, error: err});
		}
		else{
		    return res.send({success: true, message: 'User ' + uname + ' Added!'});
		}
	    });
});

// get user by userid (accessed at GET http://localhost:80/api/users)
router.get('/api/users/:id', function(req, res) {
	     //return all of the users
             console.log('returning Users');
            var sql = squel.select()
		.field("UserName")
                .from("Users")
		.where("ID = ?", req.params.id)
		.toString();
            connection.query(sql, function(err, results){
                if(err){
                        console.log(err)
                        res.send({success: 'False', error: err});
                } else {
                    console.log("Added user");
                    return res.json(results);
                }
            });
});

//get all users
router.get('/api/users/', function(req, res) {
             //return all of the users
             console.log('returning Users');
            var sql = squel.select()
                .field("UserName")
                .from("Users")
                .toString();
            connection.query(sql, function(err, results){
                if(err){
                        console.log(err)
                        res.send({success: 'False', error: err});
                } else {
                    console.log("Added user");
                    return res.json(results);
                }
            });
});


router.post('/api/login/', function(req, res){
    //attempt to login user
    h = req.headers;
    var sql = squel.select()
        .from("Users")
	.field("ID")
        .field("Username")
        .field("PasswordHash")
        .field("Salt")
	.where("Username = ?", h.uname)
	.limit(1)
        .toParam();
    connection.query(sql.text, sql.values, function(err, rows){
	if(err){
            console.log("Error Finding");
            console.log(err)
            return res.send({success: 'False', error: err});
	} else {
	    var uid = rows[0].ID;
            var salt = rows[0].Salt;
	    var passwrd = rows[0].PasswordHash;
	    var shasum = crypto.createHash('sha256');
	    shasum.update(salt + h.pass);
	    if(shasum.digest('hex') == passwrd){
	        console.log('Logging in user: ' + h.uname);
		var unamecrypt = rand(10) + uid.toString();
		res.set('cuc', unamecrypt);
		return res.send({Success: 'True'});
	    }
	    else{
		console.log('Invalid Pass');
		return res.send({Success: 'False', Error: 'passwords do not match'});
	    }
        }
    });
});


//router.post('/api/logout/', function(req, res){
//	res.clearCookie('udntf');
//	return res.render('views/home');
//});

module.exports = router;
