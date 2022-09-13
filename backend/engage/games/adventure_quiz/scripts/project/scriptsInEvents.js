
	
function showRanking(){

	
	//Create defaultModal
	var modal = document.createElement('div');
	modal.id = "modal";
	modal.style.cssText = "position:fixed;width:100%;height:100vh;opacity:1;z-index:100;top:0;left:0;right:0;margin:0 auto;border:0;"

	document.body.appendChild(modal)
	
	//Css and content elements
	modal.innerHTML = `
	<style>
	body{
		font-family: Helvetica, sans-serif;
	}
	::-webkit-scrollbar {
	  width: 5px;
	}
	::-webkit-scrollbar-track {
	  background: #f1f1f1;
	}
	::-webkit-scrollbar-thumb {
	  background: #666;
	}
	::-webkit-scrollbar-thumb:hover {
	  background: #555;
	}
	.ranking-row{display: flex;background: #FFF;margin-bottom: 1em;margin: 1em 1em;border-radius: 5px;color: #024686;font-weight: bold;justify-content: space-between;box-shadow: 1px 2px 2px 2px #c7def5;align-items: center;padding-left: 12px;}
	.ranking-row-score{background: #16a085;padding: 11px 10px;color: #FFF;}
	#top-bar{
	background: #1A6AB9;color: #FFF;display: flex;padding: 10px;font-size: 20px;justify-content: center;border-bottom: 7px solid #024686;text-shadow: 2px 2px 3px #084177;}
	#closeModal:hover{cursor:pointer;}
	#modal{background:#ddeeff;overflow-y: auto;}
	#closeModal{position: absolute;top: 0;left: 0px;background: #ff0000ba;padding: 12px 3em;font-weight: bold;font-family: arial;border-radius: 0;}
	</style>
	
	<div id="top-bar">Leaderboard</div>
	
	<svg id="loading" version="1.1" id="L9" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	  viewBox="0 0 100 100" enable-background="new 0 0 0 0" xml:space="preserve">
		<path fill="#fff" d="M73,50c0-12.7-10.3-23-23-23S27,37.3,27,50 M30.9,50c0-10.5,8.5-19.1,19.1-19.1S69.1,39.5,69.1,50">
		  <animateTransform 
			 attributeName="transform" 
			 attributeType="XML" 
			 type="rotate"
			 dur="1s" 
			 from="0 50 50"
			 to="360 50 50" 
			 repeatCount="indefinite" />
	  </path>
	</svg>
	
	<div id="closeModal">&times; Close</div>`
	
	//Event close button
	setTimeout(function(){
		loadRanking();
	}, 500);
	
}


function loadRanking(){
		var salt = "A#Ç*#$%&*+";
		var loading = document.getElementById("loading");
		loading.parentNode.removeChild(loading);
	
	    var db = firebase.firestore();
		db.collection("ranking-adventure-quiz").orderBy("score", "desc").get().then((querySnapshot) => {
		var position = 1;
	    querySnapshot.forEach((doc) => {
			
				if(sha1(doc.data().deltaT+salt+doc.data().name) === doc.data().token){
					if(doc.data().score > 0){

						modal.innerHTML += `
							<div class="ranking-row">
							<div class="ranking-row-name">${position}º ${doc.data().name}</div>
							<div class="ranking-row-score">Score: ${doc.data().score}</div>
							</div>
						`;	
						position++;		
					}
				}
			
	    });
		
		setTimeout(function(){ 
			var closeModal = document.getElementById("closeModal");
			closeModal.style.opacity="1";
			closeModal.onclick = function() {
				modal.parentNode.removeChild(modal);
			}		
		}, 500);
		
	});

}


function addRanking(name,score,runtime){
    var salt = "A#Ç*#$%&*+";
	var db = firebase.firestore();
	var deltaT = runtime.gameTime;
	var token = sha1(deltaT+salt+name); 

	db.collection("ranking-adventure-quiz").add({
	    name: name,
	    score: score,
		deltaT:deltaT,
		token:token
	})
	.then(function(docRef) {
		runtime.globalVars.scoreSubmit = true;
		runtime.globalVars.submitSuccess = true;
	})
	.catch(function(error) {
		runtime.globalVars.scoreSubmit = false;
		runtime.globalVars.submitSuccess = false;
	});
}





const scriptsInEvents = {

		async Menu_Event3_Act2(runtime, localVars)
		{
			showRanking()
		},

		async Common_Event6_Act2(runtime, localVars)
		{
			showRanking()
		},

		async Common_Event11_Act1(runtime, localVars)
		{
			addRanking(runtime.globalVars.name,runtime.globalVars.score,runtime)
		}

};

self.C3.ScriptsInEvents = scriptsInEvents;

