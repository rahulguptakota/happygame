$(document).ready(function(){var time = 0;
var running = 1;

increment();

function reset(){
	time =0;
	running =1;
	score = 0;
	document.getElementById('score_value').innerHTML = score;
}
function increment()
{
    if(running == 1){
        setTimeout(function(){
            time++;
            var mins = Math.floor(time/10/60);
            var secs = Math.floor(time/10 % 60);
            var tenths = time % 10;
           
            if(mins < 10){
                    mins = "0" + mins;
            }
            if(secs < 10){
                    secs = "0" + secs;
            }
            document.getElementById("stopwatch").innerHTML = mins + ":" + secs + ":" +  tenths + "0";
            increment();
               
        },100);
    }
}


// var totalh = 41;
// var totals = 8;
// var totala = 4;
// var totaln = 63;
var memory_array = ['A','B','C','D'];
var memory_values = [];
var memory_tile_ids = [];
var tiles_flipped = 0;
var score = parseInt($('h3#score_value').html());
var image1 = '';
var image2 = '';
var image3 = '';
var image4 = '';
var ans =0;
var level = 1;
var source1, source2, source3, source4;
Array.prototype.memory_tile_shuffle = function(){
    var i = this.length, j, temp;
    while(--i > 0){
        j = Math.floor(Math.random() * (i+1));
        temp = this[j];
        this[j] = this[i];
        this[i] = temp;
    }
}

function happyClick(num, ans){
	if(ans==num){
		$.ajax({
			type: "GET",
			url: '/facegame/getimages', 
			data: { user_level: level }, 
			success: function(data)
	    	{
               source1 = data.imagedata[1];
               source2 = data.imagedata[2];
               source3 = data.imagedata[3];
               source4 = data.imagedata[4];
	        }
	    });
		score = score + 1;
		document.getElementById('score_value').innerHTML =  score;
		var output = '';
	    memory_array.memory_tile_shuffle();
		for(var i = 0; i < memory_array.length; i++){
			if(memory_array[i] == 'A'){
				source  = source1;
				// source = document.getElementById("hidden").getAttribute("src") + "happy/p"+Math.floor(Math.random() * (totalh));
				ans = i;
			}
			else if(memory_array[i] == 'B'){
				source = source2;
				// source = document.getElementById("hidden").getAttribute("src") + "sad/p"+Math.floor(Math.random() * (totals));
			}
			else if(memory_array[i] == 'C'){
				source = source3;
				// source = document.getElementById("hidden").getAttribute("src") + "angry/p"+Math.floor(Math.random() * (totala));
			}
			else{
				source = source4;
				// source = document.getElementById("hidden").getAttribute("src") + "neutral/p"+Math.floor(Math.random() * (totaln));
			}
			output += '<div id="tile_'+i+'"><img src='+source+' height="100%" width="100%"></img></div>';
		}
		document.getElementById('memory_board').innerHTML = output;
		document.getElementById("tile_0").addEventListener ("click", function(){happyClick(0, ans)} , false);
		document.getElementById("tile_1").addEventListener ("click", function(){happyClick(1, ans)} , false);
		document.getElementById("tile_2").addEventListener ("click", function(){happyClick(2, ans)} , false);
		document.getElementById("tile_3").addEventListener ("click", function(){happyClick(3, ans)} , false);
	}
	else{
		alert("you lost.. You will play again")
		reset();
	}
}
function newBoard(){
	tiles_flipped = 0;
	var output = '';
    memory_array.memory_tile_shuffle();
    for(var i = 0; i < memory_array.length; i++){
    	if(memory_array[i] == 'A'){
			ans = i;
		}
    }

    
    $.ajax({
		type: "GET",
		url: '/facegame/getimages', 
		data: { user_level: level }, 
		success: function(data)
    	{
           source1 = data[0];
           source2 = data[1];
           source3 = data[2];
           source4 = data[3];
           // console.log(source1);
        }
    });
    console.log(source1);
	for(var i = 0; i < memory_array.length; i++){
		if(memory_array[i] == 'A'){
			source = source1;
			// source = document.getElementById("hidden").getAttribute("src")+"/happy/p"+Math.floor(Math.random() * (totalh));
		}
		else if(memory_array[i] == 'B'){
			source = source2;
			// source = document.getElementById("hidden").getAttribute("src")+"/sad/p"+Math.floor(Math.random() * (totals));
		}
		else if(memory_array[i] == 'C'){
			source = source3;
			// source = document.getElementById("hidden").getAttribute("src")+"/angry/p"+Math.floor(Math.random() * (totala));
		}
		else{
			source = source4;
			// source = document.getElementById("hidden").getAttribute("src")+"/neutral/p"+Math.floor(Math.random() * (totaln));
		}
		output += '<div id="tile_'+i+'"><img src='+source+' height="100%" width="100%"></img></div>';
		// document.getElementById("tile_"+i).onclick = happyClick(i, ans);
	}
	document.getElementById('memory_board').innerHTML = output;
	document.getElementById('score_value').innerHTML = score;
	// $('#tile_0, #tile_1, #tile_3, #tile_2').click(function(){
	//     $.post('/facegame/getimages' , {user_level: level}, 
 //    	data: {
 //               source1 = imagedata[1];
 //               source2 = imagedata[2];
 //               source3 = imagedata[3];
 //               source4 = imagedata[4];
 //           }
 //    	);
	// });
	document.getElementById("tile_0").addEventListener ("click", function(){happyClick(0, ans)} , false);
	document.getElementById("tile_1").addEventListener ("click", function(){happyClick(1, ans)} , false);
	document.getElementById("tile_2").addEventListener ("click", function(){happyClick(2, ans)} , false);
	document.getElementById("tile_3").addEventListener ("click", function(){happyClick(3, ans)} , false);

}
newBoard();
});