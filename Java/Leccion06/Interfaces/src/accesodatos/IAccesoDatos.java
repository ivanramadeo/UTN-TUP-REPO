
package accesodatos;

/**
 *
 * @author Ivan
 */
public interface IAccesoDatos {
    int MAX_REGISTRO = 10; //Atributo agregado a la interface
    
//Metodo insertar es abstracto y sin cuerpo
    void insertar();
    
    void listar();
    
    void actualizar();
    
    void elminar();
    
}
