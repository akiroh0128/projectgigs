#include <bits/stdc++.h>
using namespace std;

#define N 9

bool UnassignedLocation(int grid[N][N], int &row, int &col)
{
    for (row = 0; row < N; row++)
        for (col = 0; col < N; col++)
            if (grid[row][col] == 0)
                return true;
    return false;
}

bool InRow(int grid[N][N], int row, int num)
{
    for (int col = 0; col < N; col++)
        if (grid[row][col] == num)
            return true;
    return false;
}
 
bool InCol(int grid[N][N], int col, int num)
{
    for (int row = 0; row < N; row++)
        if (grid[row][col] == num)
            return true;
    return false;
}

bool InBox(int grid[N][N], int boxStartRow, int boxStartCol, int num)
{
    for (int row = 0; row < 3; row++)
        for (int col = 0; col < 3; col++)
            if (grid[row+boxStartRow][col+boxStartCol] == num)
                return true;
    return false;
}
 
bool toUse(int grid[N][N], int row, int col, int num)
{
    return !InRow(grid, row, num) && !InCol(grid, col, num) &&
           !InBox(grid, row - row % 3 , col - col % 3, num);
}
 
bool SolveSudoku(int grid[N][N])
{
    int row, col;
    if (!UnassignedLocation(grid, row, col))
       return true;
    for (int num = 1; num <= 9; num++)
    {
        if (toUse(grid, row, col, num))
        {
            grid[row][col] = num;
            if (SolveSudoku(grid))
                return true;
            grid[row][col] = 0;
        }
    }
    return false;
}

void printGrid(int grid[N][N])
{
    for (int row = 0; row < N; row++)
    {
        for (int col = 0; col < N; col++)
            cout<<grid[row][col]<<"  ";
        cout<<endl;
    }
}

int main()
{
    int grid[N][N] = {{2, 0, 0, 0, 0, 0, 0, 0, 0},
                      {9, 0, 0, 6, 0, 7, 0, 5, 4},
                      {0, 0, 0, 3, 4, 0, 1, 0, 0},
                      {0, 0, 0, 0, 0, 3, 7, 0, 8},
                      {0, 0, 1, 0, 2, 6, 0, 0, 0},
                      {0, 0, 0, 8, 0, 0, 9, 0, 0},
                      {0, 2, 1, 9, 8, 5, 0, 4, 0},
                      {4, 0, 0, 0, 6, 2, 5, 0, 0},
                      {6, 0, 0, 0, 0, 4, 0, 1, 0}};
    if (SolveSudoku(grid) == true)
          printGrid(grid);
    else
        cout<<"No solution exists"<<endl;
    return 0;
}