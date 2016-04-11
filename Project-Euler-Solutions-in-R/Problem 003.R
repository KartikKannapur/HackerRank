#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

is.prime  <- function(x){
  num <- ceiling(sqrt(x))
  for(i in 2:num){
    if(x%%i == 0){
      print(i)
    } 
  }
}
