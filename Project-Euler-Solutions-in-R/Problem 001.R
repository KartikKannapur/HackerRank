#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these #multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.

sum_mul_3 <- sum(seq(0,999,3))
sum_mul_5 <- sum(seq(0,999,5))
sum_mul_3and5 <- sum(seq(0,999,15))
sum_mul_3 + sum_mul_5 - sum_mul_3and5
