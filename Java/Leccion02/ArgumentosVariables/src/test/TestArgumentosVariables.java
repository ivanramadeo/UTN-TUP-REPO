
package test;


public class TestArgumentosVariables {
    public static void main(String[] args) {
        imprimirNumeros(3, 4, 5);
        imprimirNumeros(1, 2);
        variosParametros("Juan", "Perez",7,8,9);
    }

    //los argumentos variables siempre van al final de los parentesis
    private static void variosParametros(String nombre,String apellido, int ...numeros){
        System.out.println("Nombre y apellido: "+nombre+" "+apellido);
        imprimirNumeros(numeros);
    }
    
    private static void imprimirNumeros(int ...numeros){// cuando se agregan 3 puntos, es porque recibe argumentos variables
        for (int i=0; i<numeros.length;i++){
            System.out.println("Elementos: "+numeros[i]);
        }
    }
}
