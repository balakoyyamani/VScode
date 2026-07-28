const fruits = ["Apple", "Banana", "Orange"];

fruits.map((fruit)=>{
    console.log(fruit)
});

const numbers=[1,2,3,4,5];
const doubled=numbers.map((number)=>number*2);
console.log(doubled)

const students = [
  {
    id: 1,
    name: "John",
    marks: 90
  },
  {
    id: 2,
    name: "Emma",
    marks: 95
  }
];

students.map(((student)=>{
    console.log(student.name)
}));