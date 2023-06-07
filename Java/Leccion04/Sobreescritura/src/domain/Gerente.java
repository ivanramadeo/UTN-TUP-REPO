
package domain;

/**
 *
 * @author Ivan
 */
public class Gerente extends Empleado{
    private String departamento;
    public Gerente(String nombre, double sueldo, String departamento){
        super(nombre, sueldo);
        this.departamento = departamento;
    }
    //Sobreescribimos el método
    @Override 
    //Indica que el método está siendo escrito desde la clase padre
    public String obtenerDetalles(){
        return super.obtenerDetalles()+", Departamento: "+this.departamento;
    }
    
}
