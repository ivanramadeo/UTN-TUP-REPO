/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package test;

/**
 *
 * @author Ivan
 */
public class TestAutoboxingUnboxing {
    public static void main(String[] args) {
        //Clases envolventes o wrapper
        /*
        * Clases envolventes de tipos primitivos
        * int= la clase envolvente es Integer
        * long= la clase envolvente es Long
        * float= la clase envolvente es FLoat
        * double= la clase envolvente es Double
        * boolean= la clase envolvente es Boolean
        * byte= la clase envolvente es Byte
        * char= la clase envolvente es Character
        * short= la clase envolvente es Short
        * */
        int enteroPrim = 10; //tipo primitivo
        System.out.println("enteroPrim = " + enteroPrim);
        //cuando usamos las clases podemos acceder a los tipo primitivos como
        //objetos
        Integer entero = 10; // tipo object
        System.out.println("entero = " + entero.doubleValue()); //Autoboxing

        int entero2= entero;
        System.out.println("entero2 = " + entero2);

    }
}
