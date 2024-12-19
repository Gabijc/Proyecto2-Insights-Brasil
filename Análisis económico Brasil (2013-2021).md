# Índice

1. **Introducción y Resumen sobre la economía de Brasil**  
   - Estructura  
   - Órganos administrativos  
   - Balanza de pagos  
   - Comercio  

2. **Explicación del conjunto de datos**  
   - Qué contienen las columnas  
   - Objetivo del trabajo  

3. **Análisis Exploratorio de Datos (EDA)**  
   - Exploración de columnas  

4. **Análisis descriptivo**  

5. **Análisis profundo**  
   - Evolución año a año  

6. **Conclusiones y próximos pasos**  
   - Nextpoints  

## 1. Introduccion y resumen sobre la economía de Brasil

El equilibrio presupuestario es un principio que exige la nivelación de los presupeustos públicos. En este documento realizamos un análisis de la parte de los ingresos presupuestarios de Brasil entre 2013 y 2021.


## 2. Explicación del conjunto de datos

El conjunto de datos utilizado en el análisis contiene información sobre la recaudación y gestión de los ingresos públicos (fiscales y no fiscales) en Brasil entre 2013 y 2021. Los ingresos públicos en Brasil provienen de:
- Impuestos
- Contribuciones
- Tasas y tarifas
- Otros ingresos

Los ingresos públicos de Brasil se clasifican económicamente en las siguientes categorías:
- Ingresos corrientes (receitas correntes): estos ingresos pueden provenir de lo siguiente: 
   - Contribuciones(Contribuições)	
   - Impuestos, tasas y contribuciones de mejora (Impostos, Taxas e Contribuições de Melhoria)	
   - Otros ingresos corrientes (Outras Receitas Correntes)	
   - Ingresos agrícolas	(Receita Agropecuária)
   - Ingresos industriales	(Receita Industrial)
   - Ingresos Patrimoniales (Receita Patrimonial)	
   - Ingresos por Servicios (Receita de Serviços)
   - Ingresos Corrientes - a clasificar (Receitas Correntes - a classificar)	
   - Transferencias corrientes (Transferências Correntes)

- Ingresos corrientes - intrapresupuestarios: el origen de estos ingresos son los siguientes:
   - Contribuciones (Contribuições): esta cuenta se compone de las contribuciones económicas, las contribuciones a organizaciones privadas de servicios y las cotizaciones sociales (Contribuições econômicas, Contribuições para Entidades Privadas de Serv, Contribuições sociais).
   
   - Impuestos, tasas y contribuciones de mejora (Impostos, Taxas e Contribuições de Melhoria)	
   - Otros ingresos corrientes (Outras Receitas Correntes)	
   - Ingresos Industriales (Receita Industrial)
   - Ingresos Patrimoniales (Receita Patrimonial)
   - Ingresos por servicios (Receita de Serviços)
	
- Ingresos de capital: el origen de estos ingresos son los siguientes:
   - Enajenación de activos (Alienação de Bens)
   - Reembolso de préstamos (Amortizações de Empréstimos)
   - Operaciones de crédito (Operações de Crédito)
   - Otros ingresos de capital (Outras Receitas de Capital)	
   - Transferencias de capital (Transferências de Capital)

- Ingresos de capital - intrapresupuestarios: el origen de estos ingresos son los siguientes:
   - Enajenación de activos (Alienação de Bens)
   - Operaciones de crédito (Operações de Crédito)

enlace con la info de todas las categorias:
https://portal.fazenda.sp.gov.br/acessoinformacao/Downloads/Webservice/Conceitos%20de%20receitas%20LC%20131.pdf

estadisticas fiscales gobierno brasil:
https://www.tesourotransparente.gov.br/temas/estatisticas-fiscais-e-planejamento

ingresos publicos, portal transparencia: 
https://portaldatransparencia.gov.br/receitas

web tesoro nacional:
https://www.gov.br/tesouronacional/pt-br/contabilidade-e-custos/federacao/ementario-da-classificacao-por-natureza-de-receita-tabela-de-codigos


En el conjunto de datos nos encontramos la siguiente información:
- `código órgão superior`: Código numérico que identifica la entidad gubernamental superior.
- `nome órgão superior`: Nombre de la entidad gubernamental superior.
- `código órgão`: Código numérico que identifica la entidad gubernamental específica.
- `nome órgão`: Nombre de la entidad gubernamental específica.
- `código unidade gestora`: Código numérico de la unidad gestora responsable.
- `nome unidade gestora`: Nombre de la unidad gestora.
- `categoria econômica`: Clasificación económica de los ingresos (por ejemplo, "Receitas Correntes").
- `origem receita`: Fuente específica del ingreso (por ejemplo, "Outras Receitas Correntes").
- `espécie receita`: Tipo de ingreso dentro de la fuente (por ejemplo, "Demais receitas correntes").
- `detalhamento`: Detalle adicional del tipo de ingreso (por ejemplo, "Receita de honorários de advogados").
- `valor previsto atualizado`: Monto actualizado del ingreso previsto (formato texto).
- `valor lançado`: Monto que fue registrado como lanzado (formato texto).
- `valor realizado`: Monto realmente recaudado (formato texto).
- `percentual realizado`: Porcentaje de ejecución respecto al valor previsto.
- `data lançamento`: Fecha en la que se registró la ejecución del ingreso.
- `ano exercício`: Año correspondiente a la ejecución de los ingresos
	
	
	
	
	
	
	
