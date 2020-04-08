/*
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

leetcode 200

if i were to do this gain id do it the way i did countConnectedComponents
*/
//PATHRISE IMPLEMENTATION
    public int numIslands(char[][] grid) {
        /*PLAN
        - start w edge cases like if grid is empty
        - double loop create counter
        - call dfs if is 1
        - return counter
        */

        if(grid.length == 0 || grid == null)
            return 0;
        int numOfIslands = 0;
        for(int row = 0; row < grid.length; row++){
            for(int col = 0; col < grid[row].length; col++){
                if(grid[row][col] == '1')
                    numOfIslands += DFS(grid, row, col);
            }
        }
        return numOfIslands;

    }

    private int DFS(char[][] grid, int row, int col){
        /*PLAN
            - recursive call edge cases like out of bounds or if == 0 return 0
            - call dfs all four corners
            - return 1
         */

        if(row < 0 || row >= grid.length || col < 0 || col >= grid[row].length || grid[row][col] == '0'){
            return 0;
        }

        grid[row][col] = '0';

        DFS(grid, row + 1, col);
        DFS(grid, row - 1, col);
        DFS(grid, row, col + 1);
        DFS(grid, row, col - 1 );

        return 1;

    }
