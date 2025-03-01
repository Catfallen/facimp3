let foo = 42;
foo = "bar";
foo = true;
console.log(foo);

const pi = Math.PI;
console.log(pi);

//Strings 
let nome = "João";
let sobrenome = "Silva";
let frase = `Olá, ${nome}`;
console.log(frase);

//Number
let idade = 25;
let preco = 19.99;
let temperatura = -10;
console.log(idade+preco);

//Imutabilidade
let texto = "React";
//texto[0] = "r";
let novoTexto = texto.replace("R",'r');
console.log(novoTexto);

//Operadores
//Aritméticos +,-,*,/,%


//Comparação de tipos
//== comparar valores (com conversão de tipos) 5=="5" true
//=== comparar valores e tipos 5 === false


//Estrutura condicionais
//if/else
//switch

if (idade>=18){
    console.log("Maior de idade");
}else{
    console.log("Menor de idade");
}


let diaDaSemana = 1
switch(diaDaSemana){
    case 1:
        console.log("Domingo");
        break;
    default:
        console.log("Dia inválido");
}



///Laços de repetição
//for e while

console.log("for");
for(let i = 0; i<5;i++){
    console.log(i);
}

console.log("While");
let i = 0;
while(i<5){
    console.log(i);
    i++;
}

//funções


function saudacao(nome){
    return "Olá, "+nome;
}


console.log(saudacao("Maria"));


//Arrays

//push
//pop()
//map()
//filter()


let arr1 = [1,2,3,4]
arr1.push(5);
//arr1.map((el)=>el*2)
let arr2 = arr1.map((el)=>el*2);
console.log(arr2);

let pessoa = {
    nome:"Carlos",
    idade:30,
    saudacao: ()=>"Olá, "+this.nome
}
console.log(pessoa.saudacao());


const verificarPar = (num)=>{
    return num%2 == 0 ? "par":"impar";
}
console.log(verificarPar(4));