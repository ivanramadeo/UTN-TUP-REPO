
package domain;

/**
 Bloques de inicializacion estáticos y no estaticos
 se ejecutan antes del constructor
 */
public class Persona {
    private final int idPersona;
    private static int contadorPersona;

    static{ //Bloque de inicialización estático
        System.out.println("Ejecicion del bloque estático");
        ++Persona.contadorPersona;
        //No es posible acceder a atributos no estáticos
        //desde un bloque de inicialización estático
    }
    {//Bloque de inicialización NO estático(contexto dinámico)//
        System.out.println("Ejecución del bloque No estático");
        this.idPersona = Persona.contadorPersona++; //Incrementamos el atributo
         }

    public Persona(){
        System.out.println("Ejecución del construtctor");
    }

    public int getIdPersona(){
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
    
    
}

