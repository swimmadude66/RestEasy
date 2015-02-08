var express    = require('express'); 		// call express
var app        = express(); 			// define our app using express
var path       = require('path');

app.set('view engine','html');
app.engine('html', require('ejs').renderFile);
app.use(express.static(path.join(__dirname, 'views')));

var port = process.env.PORT || 80; 		// set our port

// ROUTES FOR OUR API
// =============================================================================
var login = require('./routes/login.js');
var pins = require('./routes/pins.js')
app.use(login);
app.use(pins);

//keep this last, as it will return 404
app.use(function(req, res, next){
  res.status(404);
  // respond with html page
  if (req.accepts('html')) {
    return res.render('views/404', { url: req.url });
  }
  // respond with json
  if (req.accepts('json')) {
    return res.send({ error: 'Not found' });
  }
  // default to plain-text. send()
  return res.type('txt').send('Not found');
});

app.listen(port);
console.log('Magic happens on port ' + port);
