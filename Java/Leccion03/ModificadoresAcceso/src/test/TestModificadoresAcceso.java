/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package test;

import paquete1.Clase1;
import paquete2.Clase3;

/**
 *
 * @author Ivan
 */
public class TestModificadoresAcceso {
    public static void main(String[] args) {
        Clase1 clase1 = new Clase1();
        System.out.println("clase1 = " + clase1.atributoPublic);
        clase1.metodoPublico();
        Clase3 claseHija = new Clase3();
        System.out.println("claseHija = " + claseHija);
    }
}
