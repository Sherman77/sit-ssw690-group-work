const form  = document.querySelector('#add_form');

//Create a new JavaScript Date object
var time = new Date();

var date = time.getTime();



// saving data
form.addEventListener('submit', (e) => {
    //Prevent the default action
    e.preventDefault();
    
    //Create root reference
    const ref = firebase.storage().ref();
    
    //Select the file
    const file = document.querySelector('#picture').files[0];
    
    //Set file name
    const name = file.name;
    
    //Create the task
    const task = ref.child("/Marketplace/" + name).put(file);
    
    //Put the pic to firebase 
    task
        .then(snapshort => snapshort.ref.getDownloadURL())
        .then((url) => {
            console.log(url);
            //Create record on firestore
            db.collection('Marketplace').add({
                adTitle: form.title.value,
                adDescription: form.description.value,
                adPrice: form.price.value,
                imageOne: url,
                adCategory: form.category.value,
                adStatus: "active",
                adDate: date,
        
            });
        })
        .catch(console.error);
    

})