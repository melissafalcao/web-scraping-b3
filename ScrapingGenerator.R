library('rvest')

url <- 'http://www2.bmf.com.br/pages/portal/bmfbovespa/lumis/lum-ajustes-do-pregao-ptBR.asp'
site <- read_html(url)
info_Ajuste_HTML <- html_nodes(site,'table')
info_Ajuste <- html_text(info_Ajuste_HTML)
head(info_Ajuste,20)


head(info_Ajuste_HTML)

lista_tabela <- site %>%
  html_nodes("table") %>%
  html_table(fill = TRUE)


str(lista_tabela)
head(lista_tabela[[1]], 10)

AJUSTE <- lista_tabela[[1]]
write.csv(AJUSTE, "tabela3.csv")

