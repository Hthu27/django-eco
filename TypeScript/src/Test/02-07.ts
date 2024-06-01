const student ={
  id:1,
  name: "Thu",
  age: 21,
}

// old way
// const id = student.id;
// const rest = {
//   name: "Thu",
//   age: 21,
// }

// New
const {id, ...rest} = student