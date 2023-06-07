
package test;

import domain.*;


/**
 *
 * @author Ivan
 */
public class TestSobreescritura {
    public static void main(String[] args) {
       Empleado empleado1 = new Empleado("Juan",1000);
       imprimir(empleado1);
        //System.out.println("empleado1 = " + empleado1.obtenerDetalles());
        empleado1 = new Gerente("José", 5000, "Sistemas");
        imprimir(empleado1);
        //System.out.println("gerente1 = " + gerente1.obtenerDetalles());
    }
    public static void imprimir(Empleado empleado){
        String detalles = empleado.obtenerDetalles();
        System.out.println("detalles = " + detalles);
    }
}
