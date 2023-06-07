package test;

import enumeraciones.Continentes;
import enumeraciones.Dias;

public class TestEnumeraciones {
    public static void main(String[] args) {
        //System.out.println("Dia 1: "+ Dias.LUNES);
        //indicarDiasSemana(Dias.MARTES);
        /*
        Las enumeraciones se tratan como cadenas
        no se deben utilizar comillas, se accede a trasves d
        del operador de punto*/
        System.out.println("Continente No. 4: "+ Continentes.AMERICA);
        System.out.println("No. de paises en el 4to continente: "
                +Continentes.AMERICA.getPaises());
        System.out.println("No. de habitantes en el 4to continente: "
                +Continentes.AMERICA.getHabitantes());
        //Agregar ejecución de cada uno de los continentes





    }
    private static void indicarDiasSemana(Dias dias){
        switch (dias){
            case LUNES:
                System.out.println("Primer dia de la semana");
                break;
            case MARTES:
                System.out.println("Segundo dia de la semana");
                break;
                //Agregar todos los dias de la semana
                //Agregar default
        }
    }
}
