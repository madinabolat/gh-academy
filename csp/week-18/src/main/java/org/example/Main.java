package org.example;

public class Main {
    public static void main( String args[] ) {
        System.out.println( "Hello World!" );
        int m = 2;
        int n = 2;
        int l = 2;
        int[][] matrix1 = new int[m][n];
        int[][] matrix2 = new int[n][l];
        int[][] matrix3 = new int[m][l];


        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                matrix1[i][j] = (int) (Math.random()*100);
                for (int k = 0; k < l; k++){
                    matrix2[i][j] = (int) (Math.random()*100);
                }
            }
        }

        System.out.println("Matrix 1");
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                System.out.print(matrix1[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println("Matrix 2");
        for (int i = 0; i < n; i++){
            for (int j = 0; j < l; j++){
                System.out.print(matrix2[i][j] + " ");
            }
            System.out.println();
        }

        //m x n
        //n x l
        //result: m x l
        for (int i = 0; i < m; i++){
            for (int k = 0; k < l; k++){
                for (int j = 0; j < n; j++) {
                    matrix3[i][k] += matrix1[i][j] * matrix2[j][k];
                }
            }
        }


        for (int i = 0; i < m; i++){
            for (int j = 0; j < l; j++){
                System.out.print(matrix3[i][j] + " ");
            }
            System.out.println();
        }

    }
}
