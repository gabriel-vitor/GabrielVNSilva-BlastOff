programa {	

	funcao real km_variacao(real kminicial, real kmfinal) {
		real kmtotal = kmfinal - kminicial
		retorne kmtotal
	}

	funcao inicio () { 
		real kminicial
		real kmfinal
		real litrogasolina
		real resultado
		
		escreva("informe a quilometragem inicial: ")
		leia(kminicial)

		escreva("informe a quilometragem final: ")
		leia(kmfinal)

		escreva("informe quantos litros de gasolina comprou")
		leia(litrogasolina)

		km_variacao(kminicial, kmfinal)
		resultado = km_variacao(kminicial, kmfinal) / litrogasolina
		escreva("consumiu ", resultado, "km por litro de gasolina")
		
	} 
}



/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 127; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */