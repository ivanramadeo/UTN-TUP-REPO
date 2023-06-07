/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package paquete2;

import paquete1.Clase1;

/**
 *
 * @author Ivan
 */
public class Clase3 extends Clase1 {
    public Clase3(){
        super("protected");
        this.atributoProtected = "Accedeos desde la clase hija";
        System.out.println("atributoProtected = " + this.atributoProtected);
        this.atributoPublic = "es totalmente publico";

    }
}
