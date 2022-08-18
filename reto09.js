let x=[1,2,3,4,5];
max = 0;
for (let index = 0; index < x.length; index++) {
  if (x[index]>max){
    max = x[index];
    console.log(max);
  }
}
console.log("El número más alto es " + max);
 

