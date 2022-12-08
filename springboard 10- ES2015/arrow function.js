// function double (arr) {
// return arr.map(function(val) {
// return val * 2;
//  });  
// }

// multiplying the values of the array by two
// parameters - arr    value? 
// => { 
  
   // return arr.map{
     //   val * 2;
 //   }
//  }

// my solution 
// function double(arr) {
//    return arr.map{
//        val * 2
//    }
// }
// my mistakes: the return is implied, stating this as a funciton is not necessary, use const for storage and later use for some reason included val as a parameter, being concerned it would be left out. not refactoring val * 2

const double = arr => arr.map(val => val * 2);

// function squareAndFindEvens(numbers){                 PARAMETER = NUMBERS  
//    var squares = numbers.map(function(num){           FUNCTION = CREATING VARIABLE OF NUMBERS.MAP   
            //      return num ** 2;                     FUNCTION =   NUM TO THE EXPONET OF 2
            //    });


//    var evens = squares.filter(function(square){      FUNCTION = CREATING THE FUNCTION FOR FINDING EVENS 
//      return square % 2 === 0;                        FUNCTION = RETURNING VALUES OF SQUARE WHOM ARE DIVISIBLE BY 2 W/ NO REMAINEDER 
//    });
//    return evens;
//  }

// APPROACH 
// identify the objective of the expression 
// approach to this written in CAPS 
// identify the paramters of the expression 
// identify the functions 


// MY SOLUTION 
// const squareAndEvens = numbers =>
//    square => numbers.map(num => num ** 2);  !!! this doesnt seem right, unless this is.. an example of open recursion? little lost there. 
//    evens =>  squares.filter(square % 2 === 0);

const squareAndFindEvens = numbers => numbers.map(val => val ** 2).filter(square => square % 2 === 0);

// is this numbers.map(val => val ** 2).filter(square => square % 2 === 0);  an example of object oriented programming and open recursion? 