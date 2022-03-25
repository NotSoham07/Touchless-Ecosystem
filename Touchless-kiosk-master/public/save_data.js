function myFunction(){
    var x = document.getElementById("deadmeat").value;
    sessionStorage.setItem("x", x);
    
}

function checkAll() {  
    


var A1 = document.getElementById("1A");  
var B1 = document.getElementById("1B");  
var C1 = document.getElementById("1C");  
var D1 = document.getElementById("1D");  
var E1 = document.getElementById("1E");  
var F1 = document.getElementById("1F");  
var A2 = document.getElementById("2A");  
var B2 = document.getElementById("2B");  
var C2 = document.getElementById("2C");  
var D2 = document.getElementById("2D");  
var E2 = document.getElementById("2E");  
var F2 = document.getElementById("2F");
var A3 = document.getElementById("3A");  
var B3 = document.getElementById("3B");  
var C3 = document.getElementById("3C");  
var D3 = document.getElementById("3D");  
var E3 = document.getElementById("3E");  
var F3 = document.getElementById("3F");  
var A4 = document.getElementById("4A");  
var B4 = document.getElementById("4B");  
var C4 = document.getElementById("4C");  
var D4 = document.getElementById("4D");  
var E4 = document.getElementById("4E");  
var F4 = document.getElementById("4F");  
var A5 = document.getElementById("5A");  
var B5 = document.getElementById("5B");  
var C5 = document.getElementById("5C");  
var D5 = document.getElementById("5D");  
var E5 = document.getElementById("5E");  
var F5 = document.getElementById("5F");  
var A6 = document.getElementById("6A");  
var B6 = document.getElementById("6B");  
var C6 = document.getElementById("6C");  
var D6 = document.getElementById("6D");  
var E6 = document.getElementById("6E");  
var F6 = document.getElementById("6F");  
var A7 = document.getElementById("7A");  
var B7 = document.getElementById("7B");  
var C7 = document.getElementById("7C");  
var D7 = document.getElementById("7D");  
var E7 = document.getElementById("7E");  
var F7 = document.getElementById("7F");  
var A8 = document.getElementById("8A");  
var B8 = document.getElementById("8B");  
var C8 = document.getElementById("8C");  
var D8 = document.getElementById("8D");  
var E8 = document.getElementById("8E");  
var F8 = document.getElementById("8F");  
var A9 = document.getElementById("9A");  
var B9 = document.getElementById("9B");  
var C9 = document.getElementById("9C");  
var D9 = document.getElementById("9D");  
var E9 = document.getElementById("9E");  
var F9 = document.getElementById("9F");  
var A10 = document.getElementById("10A");  
var B10 = document.getElementById("10B");  
var C10 = document.getElementById("10C");  
var D10 = document.getElementById("10D");  
var E10 = document.getElementById("10E");  
var F10 = document.getElementById("1F0");    
 
var res="";   
if (A1.checked == true){ 
res = res + "1A" + ",";   
}   
if (B1.checked == true){  
res = res + "1B" + ",";   
}  
if (C1.checked == true){  
    res = res + "1C" + ",";   
    } 
if (D1.checked == true){  
res = res + "1D" + ",";   
}
if (E1.checked == true){  
    res = res + "1E" + ",";   
    }
if (F1.checked == true){  
res = res + "1F" + ",";   
}
if (A2.checked == true){  
    res = res + "2A" + ",";   
    }
if (B2.checked == true){  
res = res + "2B" + ",";   
}     
sessionStorage.setItem("res", res);

}  

