# 1d6 game
Code that finds the solution to this stats problem:
You and your opponent play a game where you each take turns rolling 1d6 (a six sided die) and add the number rolled to your own running total. The first to reach 11 wins. You (but not your opponent) get to add +1 to each of your rolls. What is the probability that you will win if you go first? Second? What is the probability you will win if you have a 30% chance of going first?

This is the final output of running the script:
```
P1(W) = Final probability of winning for P1 = 1093853/1259712 ≈ 0.8683357783366357
P2(W) = probability of winning for P2 = 165859/1259712 ≈ 0.1316642216633643

By simply weighting these probabilities, you can find that if you have a 30% chance of going first:
P(W) = 394123169/604661760 ≈ 0.6518076635109189
```

For fun, I also implemented a version of this code using convolutions on this branch:
https://github.com/KDJDEV/1d6-game/tree/convolve