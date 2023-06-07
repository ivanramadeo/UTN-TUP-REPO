let x = 10; //variable de tipo primitiva
console.log(x.length)
console.log('Tipos primitivos')
//Objeto
let persona = {
    nombre: 'Pepe',
    apellido: 'Perez',
    email: 'pperez@mail.com',
    edad: 28,
    idioma: 'ES',
    get lang(){
        return this.idioma.toUpperCase(); //Convierte a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function () { //metodo o funcion en JavaScript
        return this.nombre + ' ' + this.apellido;
    },
    //getters y setters
    get nombreEdad() { //metodo get
        return 'El nombre es: '+this.nombre + ', edad: ' + this.edad;
    },
    

}
console.log(persona.nombre)
console.log(persona.apellido)
console.log(persona.edad)
console.log(persona.edad)
console.log(persona.email)
console.log(persona.nombreCompleto());
console.log('Ejecutando con un objeto')


let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = 'Carlos';
persona2.direccion = 'Saturno 15';
persona2.telefono = '55443322';

console.log(persona2.telefono);
console.log('Creamos un nuevo objeto')
console.log(persona['apellido']); //Accedemos como si fuera un arreglo
console.log('Accedemos como si fuera un arreglo')
//for in
for (propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}

persona.apellido = 'Lara'; //Cambiamos dinamicamente un valor del objeto
console.log(persona.apellido);

//Distintas formas de imprimir un objeto
console.log('Distintas formas de imprimir un objeto')
//Numero 1: la más sencilla: concatenar cada calor de cada propierdad
console.log('Numero 1: la más sencilla: concatenar cada calor de cada propierdad')
console.log(persona.nombre + ', ' + persona.apellido + ', ' + persona.email + ', ' + persona.edad);

//Numero 2: Utilizando un ciclo for in
console.log('Numero 2: Utilizando un ciclo for in')
for (nombrePropiedad in persona){  //nombrePropiedad es una variable que se crea en tiempo de ejecucion
    console.log(persona[nombrePropiedad]);
}
//Numero 3: Utilizando la funcion Object.values
console.log('Numero 3: Utilizando la funcion Object.values')
let personaArray = Object.values(persona);
console.log(personaArray);

//Numero 4: utilizando JSON.stringify
console.log('Numero 4: utilizando JSON.stringify')
let personaString = JSON.stringify(persona);
console.log(personaString);

//Ahora utilizaremos get y set
console.log(persona.nombreEdad)

console.log('Comenzamos con los metodos get y set para idiomas');
console.log(persona.lang);
persona.lang = 'en';
console.log(persona.lang);

//Funcion constructor de objetos de tipo Persona
console.log('Funcion constructor de objetos de tipo Persona')
function Persona3(nombre, apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre + ' ' + this.apellido;
    };
}
let padre = new Persona3('Juan', 'Perez', 'jperez@mail.com');
padre.telefono = '55443322';
console.log(padre);
console.log(padre.nombreCompleto());


let madre = new Persona3('Laura', 'Quintero', 'lquintero@mail.com');
console.log(madre);
console.log(madre.nombreCompleto());

//Diferentes formas de crear objetos
//caso objeo 1
let miObjeto = new Object(); //Opcion formal objeto vacio
//caso objeto 2
let miObjeto2 = {}; //Opcion breve y recomendada

//caso String 1
let miCadena1 = new String('Hola'); //Sintaxis formal
//caso String 2
let miCadena2 = 'Hola'; //Sintaxis simplificada y recomendada

//caso Number 1
let miNumero = new Number(1);  //Sintaxis formal
//caso Number 2
let miNumero2 = 1; //Sintaxis simplificada y recomendada

//caso Boolean 1
let miBoolean = new Boolean(false); //Sintaxis formal
//caso Boolean 2
let miBoolean2 = false; //Sintaxis simplificada y recomendada

//caso Function 1
let miFuncion = new Function(); //Todo despues de new es considerado como un objeto
//caso Function 2
let miFuncion2 = function () {}; //Sintaxis simplificada y recomendada

//caso Array 1
let miArray = new Array(); //Sintaxis formal
//caso Array 2
let miArray2 = []; //Sintaxis simplificada y recomendada


//Uso de prototype
console.log('Uso de prototype')
Persona3.prototype.telefono = '44888999202';
console.log(padre.telefono);
console.log(madre.telefono);

//Uso de call
console.log('Uso de call')
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, tel){
        return titulo + ': ' + this.nombre + ' ' + this.apellido + ', ' + tel;
        //return this.nombre + ' ' + this.apellido;
    }
}
let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'

}
console.log(persona4.nombreCompleto2('Lic', '55443322'));
console.log(persona4.nombreCompleto2.call(persona5, 'Ing', '55443322'));

//metodo Apply
console.log('metodo Apply')
let arreglo = ['Ing', '55443322'];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));






