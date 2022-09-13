
import * as CriptoJS from "./cripto.js";
import * as FirebaseApp from "./firebase-app.js";
import * as FirebaseFirestore from "./firebase-firestore.js";


runOnStartup(async runtime =>
{
	
	runtime.addEventListener("beforeprojectstart", () => OnBeforeProjectStart(runtime));
});

async function OnBeforeProjectStart(runtime)
{


	function initFirebase(runtime){
		// Initialize Cloud Firestore through Firebase
		firebase.initializeApp({
			apiKey: `${runtime.globalVars.APIKEY}`,
			authDomain: `${runtime.globalVars.authDomain}`,
			projectId: `${runtime.globalVars.projectId}`
		});	
	}
	
	initFirebase(runtime);
	


}