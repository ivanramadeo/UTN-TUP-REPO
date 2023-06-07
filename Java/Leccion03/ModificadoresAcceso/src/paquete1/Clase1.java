/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package paquete1;

/**
 *
 * @author Ivan
 */
public class Clase1 {
    public String atributoPublic = "Valor atributo public";
    protected String atributoProtected = "Valor de atributo protected";
    public Clase1(){
        System.out.println("Constructor public");

    }

    protected Clase1(String atributoProtected){
        System.out.println("Constructor protected");
    }
    public void metodoPublico(){
        System.out.println("Metodo public");
    }
    protected void metodoProtected(){
        System.out.println("Método protected");
    }

}
