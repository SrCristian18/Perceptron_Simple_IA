/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Logica;

import java.util.Scanner;


public class Perceptron {
    
    private double[] pesos;
    private double bias;
    

    public Perceptron() {
        pesos = new double[3];
        for (int i = 0; i < pesos.length; i++) {
            pesos[i] = Math.random()*2-1;
        }
        bias = Math.random()*2-1;
    }
    
    private int calcularsalidas(int[] entradas){
        double y = pesos[0] * entradas[0] + pesos[1]*entradas[1] + pesos[2]*entradas[2];
        return y > 0 ? 1: 0;
    }
    
    private void entrenar(int[][] entradas, int[] salidas){
        boolean error = true;
        while(error){
            error = false;
        for (int i = 0; i < entradas.length; i++) {
                int y = calcularsalidas(entradas[i]);
                int errorLocal = salidas[i] - y;
                for (int j = 0; j < pesos.length; j++) {
                pesos[j]+= errorLocal * entradas[i][j];
            }
                bias+= errorLocal;
                if (errorLocal !=0) {
                    error = true;
                }
            }
        }
    }
    
    public static void main(String[] args) {
        Perceptron per = new Perceptron();
        Scanner in = new Scanner(System.in);
        
        //definir las entradas, se utilizará una matriz
        int[][] entradas =
        {           
            //posiblemente no sea necesario colocarle valor de tabla al bias
            //podría funcionar sin él, y así se reduce la matriz en una columna
            {1,1,1}, //0 (1)
            {1,1,-1},//1 (2)
            {1,-1,1},//2 (3)
            {1,-1,-1},//3 (4)
            {-1,1,1},//4 (5)
            {-1,1,-1},//5 (6)
            {-1,-1,1},//6 (7)
            {-1,-1,-1},//7 (8)   
        };
        
        //salidas deseadas
        int[] salidas = {1,1,1,1,1,1,1,-1};
        
        per.entrenar(entradas, salidas);
        
        //prueba
        int[] entradasNuevas = new int[3];
        
        for (int i = 0; i <= entradasNuevas.length; i++) {
        System.out.println("Ingrese una entrada");
        entradasNuevas[i]=in.nextInt();
            
        }
                
        int salida= per.calcularsalidas(entradasNuevas);
        System.out.println("Salida es: "+salida);
    }
}
