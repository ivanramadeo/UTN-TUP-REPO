
package excepciones;

/**
 *
 * @author Ivan
 */
public class OperacionExcepcion extends RuntimeException{
    //Constructor
    public OperacionExcepcion(String mensaje){
        super(mensaje);
    }
}
