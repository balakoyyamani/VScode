const a=[1,2,3,4,5];
console.log(a)

// copying ... is spread operator
const b=[...a];
console.log(b)

const c=[6,7,8,9,0];

//combine arrays

const combine=[...a,...c];
console.log(combine)

//spread operator in objects
const person={
    name:"Bala",
    age:21
};

const updatePerson={
    ...person,
    city:"Chennai"
}

console.log(updatePerson)