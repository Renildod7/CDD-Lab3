import scrapy
import csv


class DeputadosSpider(scrapy.Spider):
    name = "deputadas"
    count = 1


    def start_requests(self):
        with open('./deputadas.csv', 'a',newline='') as f:
            f.write(",nome,genero,presenca_plenario,ausencia_plenario,ausencia_justificada_plenario,presenca_comissao,ausencia_comissao,ausencia_justificada_comissao,data_nascimento,gasto_total_par,gasto_jan_par,gasto_fev_par,gasto_mar_par,gasto_abr_par,gasto_maio_par,gasto_junho_par,gasto_jul_par,gasto_agosto_par,gasto_set_par,gasto_out_par,gasto_nov_par,gasto_dez_par,gasto_total_gab,gasto_jan_gab,gasto_fev_gab,gasto_mar_gab,gasto_abr_gab,gasto_maio_gab,gasto_junho_gab,gasto_jul_gab,gasto_agosto_gab,gasto_set_gab,gasto_out_gab,gasto_nov_gab,gasto_dez_gab,salario_bruto\n")
           
        urls = [
            "https://www.camara.leg.br/deputados/204528",
            "https://www.camara.leg.br/deputados/204545",
            "https://www.camara.leg.br/deputados/74057",
            "https://www.camara.leg.br/deputados/204353",
            "https://www.camara.leg.br/deputados/204400",
            "https://www.camara.leg.br/deputados/73696",
            "https://www.camara.leg.br/deputados/123756",
            "https://www.camara.leg.br/deputados/204509",
            "https://www.camara.leg.br/deputados/73701",
            "https://www.camara.leg.br/deputados/204374",
            "https://www.camara.leg.br/deputados/160589",
            "https://www.camara.leg.br/deputados/213762",
            "https://www.camara.leg.br/deputados/204507",
            "https://www.camara.leg.br/deputados/164360",
            "https://www.camara.leg.br/deputados/204369",
            "https://www.camara.leg.br/deputados/204380",
            "https://www.camara.leg.br/deputados/204462",
            "https://www.camara.leg.br/deputados/178928",
            "https://www.camara.leg.br/deputados/178939",
            "https://www.camara.leg.br/deputados/204459",
            "https://www.camara.leg.br/deputados/81297",
            "https://www.camara.leg.br/deputados/204434",
            "https://www.camara.leg.br/deputados/178994",
            "https://www.camara.leg.br/deputados/204421",
            "https://www.camara.leg.br/deputados/178989",
            "https://www.camara.leg.br/deputados/204525",
            "https://www.camara.leg.br/deputados/178945",
            "https://www.camara.leg.br/deputados/204357",
            "https://www.camara.leg.br/deputados/204535",
            "https://www.camara.leg.br/deputados/178961",
            "https://www.camara.leg.br/deputados/204360",
            "https://www.camara.leg.br/deputados/178946",
            "https://www.camara.leg.br/deputados/204534",
            "https://www.camara.leg.br/deputados/204464",
            "https://www.camara.leg.br/deputados/178901",
            "https://www.camara.leg.br/deputados/204466",
            "https://www.camara.leg.br/deputados/215044",
            "https://www.camara.leg.br/deputados/74784",
            "https://www.camara.leg.br/deputados/178866",
            "https://www.camara.leg.br/deputados/166402",
            "https://www.camara.leg.br/deputados/204458",
            "https://www.camara.leg.br/deputados/204471",
            "https://www.camara.leg.br/deputados/204430",
            "https://www.camara.leg.br/deputados/74398",
            "https://www.camara.leg.br/deputados/204540",
            "https://www.camara.leg.br/deputados/178956",
            "https://www.camara.leg.br/deputados/204428",
            "https://www.camara.leg.br/deputados/204432",
            "https://www.camara.leg.br/deputados/204453",
            "https://www.camara.leg.br/deputados/66179",
            "https://www.camara.leg.br/deputados/205535",
            "https://www.camara.leg.br/deputados/204377",
            "https://www.camara.leg.br/deputados/73943",
            "https://www.camara.leg.br/deputados/204529",
            "https://www.camara.leg.br/deputados/204565",
            "https://www.camara.leg.br/deputados/160639",
            "https://www.camara.leg.br/deputados/160641",
            "https://www.camara.leg.br/deputados/204467",
            "https://www.camara.leg.br/deputados/178925",
            "https://www.camara.leg.br/deputados/74075",
            "https://www.camara.leg.br/deputados/220008",
            "https://www.camara.leg.br/deputados/160575",
            "https://www.camara.leg.br/deputados/204407",
            "https://www.camara.leg.br/deputados/204354",
            "https://www.camara.leg.br/deputados/160598",
            "https://www.camara.leg.br/deputados/178966",
            "https://www.camara.leg.br/deputados/107283",
            "https://www.camara.leg.br/deputados/198197",
            "https://www.camara.leg.br/deputados/67138",
            "https://www.camara.leg.br/deputados/74848",
            "https://www.camara.leg.br/deputados/108338",
            "https://www.camara.leg.br/deputados/178839",
            "https://www.camara.leg.br/deputados/204468",
            "https://www.camara.leg.br/deputados/204546",
            "https://www.camara.leg.br/deputados/160534",
            "https://www.camara.leg.br/deputados/178832",
            "https://www.camara.leg.br/deputados/204375",
            "https://www.camara.leg.br/deputados/139285",
            "https://www.camara.leg.br/deputados/204405",
            "https://www.camara.leg.br/deputados/204410"

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
        genero = "F"
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

        with open('./deputadas.csv', 'a',newline='') as f:
            csv.writer(f, delimiter=',').writerow(row)

        self.count += 1
