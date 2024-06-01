interface Student {
  id: number;
  name: string;
  }

interface List<T> {
  length: number;
  [index: number]: T;
  }
const numbeList: List<number> = [1, 2, 3];
const wordList: List<string> = ['easy', 'frontend']

const studentList: List<Student> = [
  { id: 1, name: 'easy' },
  { id: 2, name: 'frontend' },
  ]

// key
type StudentKey = keyof Student;
const keys: StudentKey = 'id';

// type of
console.log(typeof 'easy frontend'); // 'string'
console.log(typeof 123); // 'number'
console.log(typeof false); // 'boolean'
console.log(typeof {}); // 'object'
console.log(typeof []); // 'object'
console.log(typeof function() {}); // 'function'
console.log(typeof window !== 'undefined'); // true on client, false on server


// Mapped types
type MappedTypes = {
  [Key in keyof Student]: boolean;
  };