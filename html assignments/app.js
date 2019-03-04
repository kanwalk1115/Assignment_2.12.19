// palindrome function
var word1 = "cat"
var word2 = "dad"

let isPalindrome = (string) => string == string.split('').reverse().join('');

isPalindrome(word1)
isPalindrome(word2)

console.log(isPalindrome(word1))
console.log(isPalindrome(word2))


// remove duplicates
let withDuplicates = ['a', 'b', 'c', 'd', 'd', 'a', 'e', 'f', 'g', 'b', 'b', 'h', 'i']

function removeDuplicates(arr){
    let finalArray = []
    for(let i = 0;i < arr.length; i++){
        if(finalArray.indexOf(arr[i]) == -1){
            finalArray.push(arr[i])
        }
    }
    return finalArray
}

console.log(removeDuplicates(withDuplicates));

var listOne = ['apples', 'bananas', 'orages', 'berries'];
var n = listOne.includes('kiwi')
console.log(n);


//return largest number and smallest number

var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

console.log(Math.max(...numbers));
console.log(Math.min(...numbers));

//even or odd
var num = 5

function oddEven(num){
  if (num % 2 == 0){
    console.log(even);}
  else {
    console.log(oddEven)
  }
}
console.log(oddEven(num))
