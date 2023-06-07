
package test;

import accesodatos.*;

/**
 *
 * @author Ivan
 */
public class TestInterface {
    public static void main(String[] args) {
        //desde un interface no se puede instanciar un objeto porque no tienen caracteristicas
        //tienen comportamientos
        IAccesoDatos datos = new ImplementacionMysql();
        //datos.listar();
        //imprimir(datos);
        
        datos = new ImplementacionOracle();
        //datos.listar();
        imprimir(datos);
    }
    public static void imprimir(IAccesoDatos datos){
        datos.listar();
    }
    
}
