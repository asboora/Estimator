function hidefunction(id) {
     
    
    var cb = document.getElementById(id);

    if(cb.style.display ==="block"){
        cb.style.display = "none";
        alert("displayed");
    }else{
        cb.style.display = "block";
        alert("not displayed");
    }
}