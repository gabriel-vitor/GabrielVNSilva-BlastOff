programa {	

	
	funcao inicio () { 
		real saldo = 500.00
		real cheque
		real novo_saldo
		
		escreva("seu saldo atual é: R$ ", saldo)
		escreva("\ninforme o valor do cheque: ")
		leia(cheque)

		se (cheque > saldo) 
			escreva("valor não descontado, saldo insuficiente")
		senao
			escreva("cheque descontato")
			novo_saldo = saldo - cheque
			escreva("\no novo saldo é: R$ ",novo_saldo) 
	
		}
		
}



/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 92; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */