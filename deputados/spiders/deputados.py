import scrapy
import csv


class DeputadosSpider(scrapy.Spider):
    name = "deputados"
    count = 1


    def start_requests(self):
        with open('./deputados.csv', 'a',newline='') as f:
            f.write(",nome,genero,presenca_plenario,ausencia_plenario,ausencia_justificada_plenario,presenca_comissao,ausencia_comissao,ausencia_justificada_comissao,data_nascimento,gasto_total_par,gasto_jan_par,gasto_fev_par,gasto_mar_par,gasto_abr_par,gasto_maio_par,gasto_junho_par,gasto_jul_par,gasto_agosto_par,gasto_set_par,gasto_out_par,gasto_nov_par,gasto_dez_par,gasto_total_gab,gasto_jan_gab,gasto_fev_gab,gasto_mar_gab,gasto_abr_gab,gasto_maio_gab,gasto_junho_gab,gasto_jul_gab,gasto_agosto_gab,gasto_set_gab,gasto_out_gab,gasto_nov_gab,gasto_dez_gab,salario_bruto\n")
        
        urls = [
            "https://www.camara.leg.br/deputados/204554",
            "https://www.camara.leg.br/deputados/204521",
            "https://www.camara.leg.br/deputados/204379",
            "https://www.camara.leg.br/deputados/204560",
            "https://www.camara.leg.br/deputados/121948",
            "https://www.camara.leg.br/deputados/74646,"
            "https://www.camara.leg.br/deputados/141372",
            "https://www.camara.leg.br/deputados/160508",
            "https://www.camara.leg.br/deputados/136811",
            "https://www.camara.leg.br/deputados/178835",
            "https://www.camara.leg.br/deputados/160527",
            "https://www.camara.leg.br/deputados/204495",
            "https://www.camara.leg.br/deputados/204549",
            "https://www.camara.leg.br/deputados/178836",
            "https://www.camara.leg.br/deputados/160559",
            "https://www.camara.leg.br/deputados/204413",
            "https://www.camara.leg.br/deputados/204501",
            "https://www.camara.leg.br/deputados/160511",
            "https://www.camara.leg.br/deputados/178972",
            "https://www.camara.leg.br/deputados/204571",
            "https://www.camara.leg.br/deputados/105534",
            "https://www.camara.leg.br/deputados/204544",
            "https://www.camara.leg.br/deputados/160545",
            "https://www.camara.leg.br/deputados/204503",
            "https://www.camara.leg.br/deputados/178833",
            "https://www.camara.leg.br/deputados/141431",
            "https://www.camara.leg.br/deputados/92699,"
            "https://www.camara.leg.br/deputados/204427",
            "https://www.camara.leg.br/deputados/204411",
            "https://www.camara.leg.br/deputados/141434",
            "https://www.camara.leg.br/deputados/191923",
            "https://www.camara.leg.br/deputados/204392",
            "https://www.camara.leg.br/deputados/204510",
            "https://www.camara.leg.br/deputados/204494",
            "https://www.camara.leg.br/deputados/204393",
            "https://www.camara.leg.br/deputados/74200,"
            "https://www.camara.leg.br/deputados/115746",
            "https://www.camara.leg.br/deputados/160669",
            "https://www.camara.leg.br/deputados/204473",
            "https://www.camara.leg.br/deputados/204484",
            "https://www.camara.leg.br/deputados/204527",
            "https://www.camara.leg.br/deputados/74374,"
            "https://www.camara.leg.br/deputados/204394",
            "https://www.camara.leg.br/deputados/74383,"
            "https://www.camara.leg.br/deputados/204575",
            "https://www.camara.leg.br/deputados/204491",
            "https://www.camara.leg.br/deputados/74270,"
            "https://www.camara.leg.br/deputados/204365",
            "https://www.camara.leg.br/deputados/160673",
            "https://www.camara.leg.br/deputados/178996",
            "https://www.camara.leg.br/deputados/198783",
            "https://www.camara.leg.br/deputados/161550",
            "https://www.camara.leg.br/deputados/207309",
            "https://www.camara.leg.br/deputados/132504",
            "https://www.camara.leg.br/deputados/204537",
            "https://www.camara.leg.br/deputados/160640",
            "https://www.camara.leg.br/deputados/204482",
            "https://www.camara.leg.br/deputados/178871",
            "https://www.camara.leg.br/deputados/178930",
            "https://www.camara.leg.br/deputados/178953",
            "https://www.camara.leg.br/deputados/211866",
            "https://www.camara.leg.br/deputados/141428",
            "https://www.camara.leg.br/deputados/68720,"
            "https://www.camara.leg.br/deputados/178969",
            "https://www.camara.leg.br/deputados/141427",
            "https://www.camara.leg.br/deputados/171623",
            "https://www.camara.leg.br/deputados/204368",
            "https://www.camara.leg.br/deputados/160587",
            "https://www.camara.leg.br/deputados/66828,"
            "https://www.camara.leg.br/deputados/204477",
            "https://www.camara.leg.br/deputados/72442,"
            "https://www.camara.leg.br/deputados/204398",
            "https://www.camara.leg.br/deputados/204371",
            "https://www.camara.leg.br/deputados/160666",
            "https://www.camara.leg.br/deputados/212504",
            "https://www.camara.leg.br/deputados/109429",
            "https://www.camara.leg.br/deputados/141335",
            "https://www.camara.leg.br/deputados/204358",
            "https://www.camara.leg.br/deputados/178948",
            "https://www.camara.leg.br/deputados/204388",
            "https://www.camara.leg.br/deputados/141513",
            "https://www.camara.leg.br/deputados/204561",
            "https://www.camara.leg.br/deputados/204397",
            "https://www.camara.leg.br/deputados/160538",
            "https://www.camara.leg.br/deputados/74052,"
            "https://www.camara.leg.br/deputados/204551",
            "https://www.camara.leg.br/deputados/204502",
            "https://www.camara.leg.br/deputados/93083,"
            "https://www.camara.leg.br/deputados/204352",
            "https://www.camara.leg.br/deputados/204572",
            "https://www.camara.leg.br/deputados/178829",
            "https://www.camara.leg.br/deputados/204531",
            "https://www.camara.leg.br/deputados/178924",
            "https://www.camara.leg.br/deputados/204487",
            "https://www.camara.leg.br/deputados/141401",
            "https://www.camara.leg.br/deputados/204361",
            "https://www.camara.leg.br/deputados/178962",
            "https://www.camara.leg.br/deputados/178993",
            "https://www.camara.leg.br/deputados/204460",
            "https://www.camara.leg.br/deputados/74262,"
            "https://www.camara.leg.br/deputados/204516",
            "https://www.camara.leg.br/deputados/178927",
            "https://www.camara.leg.br/deputados/178937",
            "https://www.camara.leg.br/deputados/178881",
            "https://www.camara.leg.br/deputados/204356",
            "https://www.camara.leg.br/deputados/178831",
            "https://www.camara.leg.br/deputados/74471,"
            "https://www.camara.leg.br/deputados/204423",
            "https://www.camara.leg.br/deputados/133439",
            "https://www.camara.leg.br/deputados/178882",
            "https://www.camara.leg.br/deputados/204515",
            "https://www.camara.leg.br/deputados/74212,"
            "https://www.camara.leg.br/deputados/160553",
            "https://www.camara.leg.br/deputados/73433,"
            "https://www.camara.leg.br/deputados/141391",
            "https://www.camara.leg.br/deputados/204414",
            "https://www.camara.leg.br/deputados/160541",
            "https://www.camara.leg.br/deputados/160600",
            "https://www.camara.leg.br/deputados/159237",
            "https://www.camara.leg.br/deputados/74090,"
            "https://www.camara.leg.br/deputados/74459",
            "https://www.camara.leg.br/deputados/160665",
            "https://www.camara.leg.br/deputados/160512",
            "https://www.camara.leg.br/deputados/69871,"
            "https://www.camara.leg.br/deputados/178975",
            "https://www.camara.leg.br/deputados/74060,"
            "https://www.camara.leg.br/deputados/178916",
            "https://www.camara.leg.br/deputados/204367",
            "https://www.camara.leg.br/deputados/204454",
            "https://www.camara.leg.br/deputados/204409",
            "https://www.camara.leg.br/deputados/160528",
            "https://www.camara.leg.br/deputados/62881,"
            "https://www.camara.leg.br/deputados/160552",
            "https://www.camara.leg.br/deputados/116379",
            "https://www.camara.leg.br/deputados/73891,"
            "https://www.camara.leg.br/deputados/205548",
            "https://www.camara.leg.br/deputados/204511",
            "https://www.camara.leg.br/deputados/204451",
            "https://www.camara.leg.br/deputados/178908",
            "https://www.camara.leg.br/deputados/204512",
            "https://www.camara.leg.br/deputados/204569",
            "https://www.camara.leg.br/deputados/164359",
            "https://www.camara.leg.br/deputados/204542",
            "https://www.camara.leg.br/deputados/213856",
            "https://www.camara.leg.br/deputados/160588",
            "https://www.camara.leg.br/deputados/178929",
            "https://www.camara.leg.br/deputados/160599",
            "https://www.camara.leg.br/deputados/143632",
            "https://www.camara.leg.br/deputados/160758",
            "https://www.camara.leg.br/deputados/204450",
            "https://www.camara.leg.br/deputados/204426",
            "https://www.camara.leg.br/deputados/141398",
            "https://www.camara.leg.br/deputados/204499",
            "https://www.camara.leg.br/deputados/204370",
            "https://www.camara.leg.br/deputados/178876",
            "https://www.camara.leg.br/deputados/204488",
            "https://www.camara.leg.br/deputados/141405",
            "https://www.camara.leg.br/deputados/73441,"
            "https://www.camara.leg.br/deputados/204496",
            "https://www.camara.leg.br/deputados/204504",
            "https://www.camara.leg.br/deputados/205476",
            "https://www.camara.leg.br/deputados/204490",
            "https://www.camara.leg.br/deputados/141439",
            "https://www.camara.leg.br/deputados/204476",
            "https://www.camara.leg.br/deputados/204440",
            "https://www.camara.leg.br/deputados/74537,"
            "https://www.camara.leg.br/deputados/141408",
            "https://www.camara.leg.br/deputados/204376",
            "https://www.camara.leg.br/deputados/204378",
            "https://www.camara.leg.br/deputados/204514",
            "https://www.camara.leg.br/deputados/178963",
            "https://www.camara.leg.br/deputados/135054",
            "https://www.camara.leg.br/deputados/204355",
            "https://www.camara.leg.br/deputados/141411",
            "https://www.camara.leg.br/deputados/74467,"
            "https://www.camara.leg.br/deputados/213854",
            "https://www.camara.leg.br/deputados/204518",
            "https://www.camara.leg.br/deputados/212625",
            "https://www.camara.leg.br/deputados/204481",
            "https://www.camara.leg.br/deputados/213679",
            "https://www.camara.leg.br/deputados/204439",
            "https://www.camara.leg.br/deputados/204351",
            "https://www.camara.leg.br/deputados/178830",
            "https://www.camara.leg.br/deputados/204412",
            "https://www.camara.leg.br/deputados/204562",
            "https://www.camara.leg.br/deputados/141417",
            "https://www.camara.leg.br/deputados/134812",
            "https://www.camara.leg.br/deputados/74655,"
            "https://www.camara.leg.br/deputados/204541",
            "https://www.camara.leg.br/deputados/92346,"
            "https://www.camara.leg.br/deputados/204552",
            "https://www.camara.leg.br/deputados/204500",
            "https://www.camara.leg.br/deputados/178977",
            "https://www.camara.leg.br/deputados/141421",
            "https://www.camara.leg.br/deputados/141422",
            "https://www.camara.leg.br/deputados/154919",
            "https://www.camara.leg.br/deputados/204364",
            "https://www.camara.leg.br/deputados/160532",
            "https://www.camara.leg.br/deputados/204389",
            "https://www.camara.leg.br/deputados/178854"

        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        row = []

        meses = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV','DEZ']

        
        presencas = [x.strip().split()[0] for x in response.css('div.list-table ul.list-table__content dd::text').getall()]
        informacoes_deputado = [x.strip() for x in  response.css('div.fundo-1.l-identificacao-bloco ul.informacoes-deputado li::text').getall()]

        nome = informacoes_deputado[0]
        self.log(nome)
        genero = "M"
        self.log(genero)
        presença_plenario = presencas[0]
        self.log(presença_plenario)
        ausencia_plenario = presencas[1]
        self.log(ausencia_plenario)
        ausencia_justificada_plenario = presencas[2]
        self.log(ausencia_justificada_plenario)
        presenca_comissao = presencas[3]
        self.log(presenca_comissao)
        ausencia_comissao = presencas[4]
        self.log(ausencia_comissao)
        ausencia_justificada_comissao = presencas[5]
        self.log(ausencia_justificada_comissao)
        data_nascimento = informacoes_deputado[4]
        self.log(data_nascimento)


        gastos = response.css("section#gastos-section.gastos-deputado.js-gastos-conteiner ul.gastos-anuais-deputado-container li.gasto")

        gasto_total_par = gastos.css("table#percentualgastocotaparlamentar td::text").getall()[1].strip()
        gasto_mensal_par = {}


        cont = 0
        aux = ""
        for x in gastos.css("table#gastomensalcotaparlamentar tr td::text").getall():
            if (cont == 0):
                aux = x
                self.log(x)
            if (cont == 1):
                gasto_mensal_par[aux] = x
                self.log(x)
            cont = (cont + 1) % 3
        
        self.log(gasto_mensal_par)
        
        gasto_total_gab = gastos.css("table#percentualgastoverbagabinete td::text").getall()[1].strip()
        
        gasto_mensal_gab = {}

        for x in gastos.css("table#gastomensalverbagabinete tr td::text").getall():
            if (cont == 0):
                aux = x
                self.log(x)
            if (cont == 1):
                gasto_mensal_gab[aux] = x
                self.log(x)
            cont = (cont + 1) % 3

        self.log(gasto_mensal_gab)

        salario_bruto = response.css("section#recursos-section.recursos-deputado.js-recursos-beneficios-conteiner div.beneficio a.beneficio__info::text").getall()[1].split()[1]

        self.log(salario_bruto)

        row.append(nome)
        row.append(genero)
        row.append(presença_plenario)
        row.append(ausencia_plenario)
        row.append(ausencia_justificada_plenario)
        row.append(presenca_comissao)
        row.append(ausencia_comissao)
        row.append(ausencia_justificada_comissao)
        row.append(data_nascimento)
        row.append(gasto_total_par)

        for mes in (meses):
            if(mes in gasto_mensal_par.keys()):
                row.append(gasto_mensal_par[mes])
            else:
                row.append("")

        row.append(gasto_total_gab)

        for mes in (meses):
            if(mes in gasto_mensal_gab.keys()):
                row.append(gasto_mensal_gab[mes])
            else:
                row.append("")


        row.append(salario_bruto)

        self.log(row)

        row = [self.count] + row

        with open('./deputados.csv', 'a',newline='') as f:
            csv.writer(f, delimiter=',').writerow(row)

        self.count +=1
