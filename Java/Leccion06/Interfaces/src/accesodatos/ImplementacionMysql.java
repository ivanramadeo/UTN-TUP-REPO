
package accesodatos;

/**
 *
 * @author Ivan
 */
public class ImplementacionMysql implements IAccesoDatos{
    //si usaramos abstract no sería necesario implementar los métodos
    //como queremos usar las clases hijas no podemos usar abstract
    @Override
    public void insertar() {
        System.out.println("Insertar desde Mysql");
    }

    @Override
    public void listar() {
        System.out.println("Listar desde Mysql");
    }

    @Override
    public void actualizar() {
        System.out.println("Actualizar desde Mysql");
    }

    @Override
    public void elminar() {
        System.out.println("Eliminar desde Mysql");
    }
    
}
