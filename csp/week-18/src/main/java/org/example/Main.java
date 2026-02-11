package org.example;

public class Main {
    public static void main( String args[] ) {
        System.out.println( "Hello World!" );
        int m = 2;
        int n = 2;
        int l = 2;
        int[][] matrix1 = new int[m][n];
        int[][] matrix2 = new int[n][l];


        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                matrix1[i][j] = (int) (Math.random()*100);
                System.out.print(matrix1[i][j] + " ");
            }
            System.out.println();
        }

        for (int i = 0; i < n; i++){
            for (int j = 0; j < l; j++){
                matrix2[i][j] = (int) (Math.random()*100);
                System.out.print(matrix2[i][j] + " ");
            }
            System.out.println();
        }
    }
}
