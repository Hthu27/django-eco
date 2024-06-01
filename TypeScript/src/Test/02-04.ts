// ==, number

// ===, giữ nguyên

// object, array, function laf tham chiếu => ss địa chỉ tham chiếu
const studentA= {id:1, name: "Thu"};
const studentC= {id:1, name: "Thu"};
const studentB = studentA
// true
studentA === studentB
// false
// studentA === {id:1, name: "Thu"};

// true, compare the id
studentA.id === studentC.id

// check undefined
let teacher;
// fetch data
teacher = {
  id:1,
  name: "A"
}
if(teacher){}

// check empty
let doctor;
// fetch data
doctor = {
  id:1,
  name: "A"
}
if(doctor?.id){}


// check global
if(typeof window !== "undefined"){
  
}