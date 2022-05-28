from  decimal  import  getcontext , Decimal  as  dec , ROUND_UP
LATAS  =  18
GALOES  =  3,6
PRECO_LATA  =  80,0
PRECO_GALOES  =  25,0



metro_quadrado  =  float ( input ( "Forneca quantos metros quadrados a serem pintados aproximadamente \n " ))
metro_quadrado  += ( metro_quadrado  *  0.1 ) /  6  #acrescentado 10%
if  metro_quadrado  %  LATAS  ==  17 :
    latas_m_lata  = ( metro_quadrado  +  1 ) %  LATAS  # arredondar para 18 latas mais :
    latas_m_lata  =  metro_quadrado   %  LATAS
    qtd_latas_com_galoes  = ( metro_quadrado  -  latas_m_lata ) /  LATAS
    qtd_latas_com_galoes  =  dec ( qtd_latas_com_galoes ). quantize ( dec ( '1.' ), arredondamento = ROUND_UP )
    preco_misturados  =  dec ( str ( qtd_latas_com_galoes )) *  dec ( str ( PRECO_LATA ))

    qtd_galoes_com_latas  =  latas_m_lata  /  GALOES
    qtd_galoes_com_latas  =  dec ( qtd_galoes_com_latas ). quantize ( dec ( '1.' ), arredondamento = ROUND_UP )
    preco_misturados  +=  dec ( str ( qtd_galoes_com_latas )) *  dec ( str ( PRECO_GALOES ))

    preco_misturados  =  f' { preco_misturados : .2f } ' . substitua ( '.' , ',' )

    apenas_latas  =  metro_quadrado   /  LATAS
    apenas_latas  =  dez ( apenas_latas ). quantize ( dec ( '1.' ), arredondamento = ROUND_UP )
    preco_ap_latas  =  apenas_latas  *  dez ( PRECO_LATA )
    preco_ap_latas  = f' { preco_ap_latas : .2f } ' . replace ( '.' , ',' ) # 0,00 evita saída como notação 8E+1

    apenas_galoes   =  metro_quadrado   /  GALOES
    apenas_galoes  =  dez ( apenas_galoes ). quantize ( dec ( '1.' ), arredondamento = ROUND_UP )
    preco_ap_galoes  =  apenas_galoes  *  dec ( PRECO_GALOES )

    preco_ap_galoes  =  f' { preco_ap_galoes : .2f } ' . substitua ( '.' , ',' )
    print ( preco_ap_galoes )
    print ( f"Latas 18L Quantidade: { apenas_latas }   Preço total R$: { preco_ap_latas } para { metro_quadrado :1.2f } m²" )
    print ( f"Galões 3,6L Quantidade: { apenas_galoes } Preço total R$: { preco_ap_galoes } para { metro_quadrado :1.2f } m²" )
    print ( f"Galões 3,6L Quantidade: { qtd_galoes_com_latas } Latas 18L Quantidade: { qtd_latas_com_galoes } Preço total R$: { preco_misturados } para { metro_quadrado :1.2f } m²" )
