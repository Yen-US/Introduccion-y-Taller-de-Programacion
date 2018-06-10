package sumamatriz;

import java.util.Arrays;
import java.util.Scanner;

public class SumaMatriz {
        public void imprimirArray(int[] vector){
        for(int valor: vector){
            System.out.println("El valor es " + valor);
        }
    }
    public int[] llenarArray(){
        int[] lista = new int[5];
        Scanner entrada = new Scanner(System.in);
        for(int contador = 0; contador < lista.length; contador++){
            System.out.println("Ingrese el valor del array para la posición " 
                                + contador);
            lista[contador] = entrada.nextInt();
        }
        return lista;
    }
    public int[] sumarArrays(int[] lista1){
        int[] listaSuma = new int[lista1.length];
        for(int contador = 0; contador < lista1.length; contador++){
            listaSuma[contador] += lista1[contador];
        }
        return listaSuma;
    }    
    public static void main(String[] args){
        SumaMatriz list = new SumaMatriz();
        int[] list1 = list.llenarArray();
        System.out.println("Llenar valores del array"+ Arrays.toString(list1));
    }
}

