/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Logica;

import java.util.Random;
import java.util.Scanner;

public class Perceptron {
    public static void main(String[] args) {
        
        //definir las entradas, se utilizará una matriz
        double [][] entradas =
        {
            /*la primera columna corresponde al bias (que su combinación será de 1)
            esto no afectará en los cálculos, ya que su peso es el relevante.
            El resto de columnas son las entradas comunues (X1,X2,X3)
            */
            
            //posiblemente no sea necesario colocarle valor de tabla al bias
            //podría funcionar sin él, y así se reduce la matriz en una columna
            {1,1,1,1}, //0 (1)
            {1,1,1,-1},//1 (2)
            {1,1,-1,1},//2 (3)
            {1,1,-1,-1},//3 (4)
            {1,-1,1,1},//4 (5)
            {1,-1,1,-1},//5 (6)
            {1,-1,-1,1},//6 (7)
            {1,-1,-1,-1},//7 (8)
            
        };
        
        //salidas deseadas
        double[] salidas = new double[8];
            salidas[0] = 1; //1
            salidas[1] = 1;//2
            salidas[2] = 1;//3
            salidas[3] = 1;//4
            salidas[4] = 1;//5
            salidas[5] = 1;//6
            salidas[6] = 1;//7
            salidas[7] = -1;//8
        
        //definir los pesos de las entradas y el bias
        double w0 = new Random().nextDouble(); //peso del bias
        double w1 = new Random().nextDouble(); //peso de X1
        double w2 = new Random().nextDouble(); //peso de X2
        double w3 = new Random().nextDouble(); // peso de X3
        
        //se definen las variables auxiliares y del proceso
        double y = 0.0;
        double error = 0.0;
        int fila = 0;
        int iteracion = 1;
        
        
        //Depuracion
        
            System.out.println("Perceptron NAND");
            System.out.println("Peso bias: "+w0);
            System.out.println("Peso x1: "+w1);
            System.out.println("Peso x2: "+w2);
            System.out.println("Peso x3: "+w3);
            System.out.println("Iteracion: "+iteracion);

        
    
        //calculo de la salida parcial
        
        while(fila<8){
            //depuracion
            System.out.println("y =("+w0+"*"+entradas [fila][0]+") + ("+w1+"*"+entradas [fila] [1]+") + "
                    + "("+w2+"*"+entradas[fila][2]+") + ("+w3+"*"+entradas [fila][3]+")");
            y = w0*entradas[fila][0] + w1*entradas[fila][1] + w2*entradas[fila][2] + w3*entradas[fila][3];
                
                //podría dar igual sin calcular el valor de la entrada del bias
            //y = w0 + w1*entradas[fila][1] + w2*entradas[fila][2] + w3*entradas[fila][3];
            
            System.out.println("y = "+y);
            
            //funcion de activacion
            if(y>= 0){
                y=1;
                System.out.println("Como y>=0 entonces");
            }else if(y<0){
                System.out.println("Como y<0 entonces");
            }
            
            //obtener el error
            System.out.println("y= "+y);
            error = salidas[fila] - y;
            
            System.out.println("Error= "+error);
            
            //recalcular los pesos o no, dependiendo el error
            
            //si no hay error, no se recalcula
            if(error == 0.0){
                System.out.println("No hay que recalcular los pesos");
                fila++;
            }else{
                
                //si hay error, se recalcula
                if(error != 0.0){
                    System.out.println("Recalcular los pesos de "+(fila+1));
                    
                    //recalculado
                    w1=w1+(error*entradas[fila][1]); //peso x1
                    w2=w2+(error*entradas[fila][2]); //peso x2
                    w3=w3+(error*entradas[fila][3]); //peso x3
                        //formula del video
                //    w0=w0+(error*entradas[fila][0]); //peso del bias
                    //formula de Ospina
                w0=w0+error; //peso del bias
                    
                    //pesos actualizados
                    System.out.println("Nuevo peso de x1: "+w1);
                    System.out.println("Nuevo peso de x2: "+w2);
                    System.out.println("Nuevo peso de x3: "+w3);
                    System.out.println("Nuevo peso del bias: "+w0);
                    
                }
            //se reinicia el contador de fila para empezar otra iteracion
            fila = 0;
            iteracion++;
                System.out.println("");
                System.out.println("Iteracion: "+iteracion);
            }
        }
        //depuracion
        //se muestran los pesos seguros para la red entrenada
        System.out.println("");
        System.out.println("Pesos finales");
        System.out.println("Peso x1: "+w1);
        System.out.println("Peso x1: "+w2);
        System.out.println("Peso x1: "+w3);
        System.out.println("Peso bias: "+w0);
        
        //comprobación que las entradas ingresadas cumplan con la tabla NAND
        
        Scanner in = new Scanner(System.in);
        int entrada1 = 0,entrada2 = 0, entrada3 = 0;
        
        System.out.println("Ingrese la entrada 1 (1, -1): ");
        entrada1 = in.nextInt();

        System.out.println("Ingrese la entrada 2 (1, -1): ");
        entrada2 = in.nextInt();

        System.out.println("Ingrese la entrada 3 (1, -1): ");
        entrada3 = in.nextInt();
        
        //no es necesario el producto del bias
//        y= w0+(w1*entrada1)+(w2*entrada2)+(w3*entrada3)
        y = (w0*1)+(w1*entrada1)+(w2*entrada2)+(w3*entrada3);
        
        if(y >= 0)
        {
            y = 1;
        }else if(y < 0){
            y = -1;
        }
        
        System.out.println("La salida es: \n"+
                y);
        
    }
}
