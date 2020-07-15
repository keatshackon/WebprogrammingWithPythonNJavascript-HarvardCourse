
document.addEventListener('DOMContentLoaded',function(){
   document.querySelector('button').onclick = count;
});

let c=1;

function count(){
   c++;
   document.querySelector("#counter").innerHTML = c

   if(c%5 === 0){
      alert(`You Reached at ${c}`)
   }
}
