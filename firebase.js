
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-firestore.js";

// Firebase Configuration (Replace with your credentials)
const firebaseConfig = {
    apiKey: "AIzaSyC7eWdGSPDmUi9VrxkwwECv4ker9wd-PaQ",
    authDomain: "fitness-tracker-c8e21.firebaseapp.com",
    projectId: "fitness-tracker-c8e21",
    storageBucket: "fitness-tracker-c8e21.appspot.com",
    messagingSenderId: "928199593189",
    appId: "1:928199593189:web:788aaf44cf330b33c9580c"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
