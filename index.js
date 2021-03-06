const express = require('express');
const app     = express();
const port    = 	process.env.PORT || 80;
const path = require('path');
const ejs = require('ejs');
const bodyParser = require("body-parser");
const request = require("request")
const router = express.Router();
const spawn = require("child_process").spawn;


app.use(express.static(path.join(__dirname, 'public')));

app.use(bodyParser.urlencoded({
    extended: false
}));

app.use(bodyParser.json());

app.set('view engine', 'ejs');

//Define Routes below
router.get('/', function(req, res) {
	res.render('../public/page/home', {});
});

router.post('/', function(req, res) {
	console.log(req.body.github);
	const pythonProcess = spawn('python', ["./importRequests.py", req.body.github]);
	pythonProcess.stdout.on('data', (data) => {


		
	

		console.log(data.toString());
	

	



		//var uint8arrayToString = function(data){
		//	return String.fromCharCode.apply(null, data);
		//}
		//var follow = (uint8arrayToString(data));
		//console.log(follow);


		//var followers = (data.toString());
		//console.log(followers);
	});
	res.render('../public/page/home', {});
});

//Apply the routes to our application
app.use('/', router);


//START THE SERVER
//==================================================================================
app.listen(port, '0.0.0.0');
console.log('Server open at  localhost:' + port);
module.exports = router;