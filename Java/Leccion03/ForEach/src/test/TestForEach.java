/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package test;

import domain.Persona;

/**
 *
 * @author Ivan
 */
public class TestForEach {
    public static void main(String[] args) {
        int edades[] = {5,6,7,9}; //Sintaxis resumida
        // for (int i= 0; i<edades.length; i++){}
        for (int edad: edades){//Sintaxis del ForEach
            System.out.println("edad= "+edad);

        }

        Persona personas[] = {new Persona("Juan"), new Persona("Carla"), new Persona("Beatriz")};
        
        //ForEach
        for(Persona persona: personas){
            System.out.println("persona = " + persona);
        }
    }
}
