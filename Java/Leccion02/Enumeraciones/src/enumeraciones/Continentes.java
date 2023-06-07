package enumeraciones;

public enum Continentes {
    AFRICA(53, "1.25 billones"),
    EUROPA(46, "1.2 billones"),
    ASIA(44, "3 billones"),
    AMERICA(34, "1 billones"),
    OCEANIA(14, "0.5 billones");

    private final int paises;
    private String habitantes;
    Continentes(int paises, String habitantes){
        this.paises = paises;
        this.habitantes = habitantes;
    }

    //Metodo Get
    public int getPaises(){
        return this.paises;
    }
    public String getHabitantes(){
        return this.habitantes;
    }
}
