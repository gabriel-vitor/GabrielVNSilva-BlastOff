programa {	

	
	funcao inicio () { 
		real salario
		real financiamento
		real aprov_financiamento
		
		escreva("informe seu salario: ")
		leia(salario)

		escreva("informe o valor do financiamento")
		leia(financiamento)

		aprov_financiamento = salario * 5

		se (financiamento <= aprov_financiamento) 
			escreva("financiamento concedido")
		senao
			escreva("financiamento negado")
			
		escreva("\nObrigado por nos consultar")
		}
		
}



/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 234; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */