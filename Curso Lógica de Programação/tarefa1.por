programa 
{	

	funcao real bonus(inteiro quant_soft) {
		real bonusfinal = quant_soft * 50.00
		retorne bonusfinal
	} 

		
	funcao inicio () 
	{ 
		real fixo = 500.00
		inteiro numero
		real salario_final
		
		escreva("Quantos sistemas você vendeu? ")
		leia(numero)

		salario_final = fixo + bonus(numero)
		escreva("Seu salario final é R$ ", salario_final)

		
	} 
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 368; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */