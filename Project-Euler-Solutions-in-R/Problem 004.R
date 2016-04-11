#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is #9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

is.pal <- function(x) {
  pal <- 0
  x <- as.character(x)
  forward <- unlist(strsplit(x, split =""))
  reverse <- rev(forward)
  if (all(forward == reverse)) {
    pal <- 1
  }
  return(pal)
}
max <- 0
for (i in 100:999) {
  for (j in 100:999) {
    if (is.pal(i*j) == 1 & i*j > max) {
      max <- i*j
    } 
  }
}
max
