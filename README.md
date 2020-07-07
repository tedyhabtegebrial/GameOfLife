# GameOfLife with the a single kernel convolution

```
$ python3.6 play.py
```

A simple implementation of game of life.

This is implementation performs cell update by calcualting the number of neighbours for each cell by ***convolving*** the current world-state with the "*game-of-life-kernel*".

World State:   ![](state.png)

Game of life kernel:  ![](gofl_kernel.png)

