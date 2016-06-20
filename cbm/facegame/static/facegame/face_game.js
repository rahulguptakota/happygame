$(document).ready(function(){
var time = 0;
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

var memory_array = ['A','B','C','D'];

Array.prototype.memory_tile_shuffle = function(){
    var i = this.length, j, temp;
    while(--i > 0){
        j = Math.floor(Math.random() * (i+1));
        temp = this[j];
        this[j] = this[i];
        this[i] = temp;
    }
}

var ans =0;
var opt=0;
var level = 1;
var output = '';
var source1, source2, source3, source4;
var score = parseInt($('h3#score_value').html()) - 1;
var con_correct =-1;
var root_src;
function myfunc(){
	if(ans == opt){
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
				root_src = data[4];
				output = '';
			    memory_array.memory_tile_shuffle();
			    for(var i = 0; i < memory_array.length; i++){
			    	if(memory_array[i] == 'A'){
						ans = i;
					}
			    }
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
					output += '<div id=\"tile_'+i+'\"><img src=\"'+source+'\" height=\"100%\" width=\"100%\"></img></div>';
					// document.getElementById("tile_"+i).onclick = happyClick(i, ans);
				}
				score = score + 1;
				con_correct = con_correct + 1;
				if(con_correct ==4){
					if(level<3){
						level++;
					}
				}
				document.getElementById('memory_board').innerHTML = output;
				document.getElementById('score_value').innerHTML = score;
		    	document.getElementById("tile_0").addEventListener ("click", function(){ opt =0;myfunc(); } , false);
				document.getElementById("tile_1").addEventListener ("click", function(){ opt = 1;myfunc(); } , false);
				document.getElementById("tile_2").addEventListener ("click", function(){ opt = 2;myfunc(); } , false);
				document.getElementById("tile_3").addEventListener ("click", function(){ opt = 3;myfunc(); } , false);

			}
	    });
	}
	else{
		alert("you lost.. You will play again")
		reset();
		ans =0;
		opt =0;
		con_correct =0;
		myfunc();
	}
}
myfunc();
});