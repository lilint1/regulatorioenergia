from Modelos.instituicoes import MME_extracao, ANEEL_extracao, EPE_extracao, ANP_extracao


def main():
    print('')
    print('NOTÍCIAS DO MINISTERIO DE MINAS E ENERGIA - MME')
    print('')
    site_mme = MME_extracao()
    site_mme.listar_noticias()

    print('')
    print('NOTÍCIAS DA AGÊNCIA NACIONAL DE ENERGIA ELÉTRICA - ANEEL')
    print('')
    site_aneel = ANEEL_extracao()
    site_aneel.listar_noticias()

    print('')
    print('NOTÍCIAS DA AGÊNCIA NACIONAL DO PETRÓLEO, GÁS NATURAL E BIOCMBUSTÍVEIS - ANP')
    print('')
    site_anp = ANP_extracao()
    site_anp.listar_noticias()

    print('')
    print('NOTÍCIAS DA EMPRESA DE PESQUISA ENERGÉTICA - EPE')
    print('')
    site_epe = EPE_extracao()
    site_epe.listar_noticias()

if __name__ == '__main__':
    main()