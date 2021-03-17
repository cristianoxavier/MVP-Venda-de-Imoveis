# MVP-Venda-de-Imoveis
Um projeto MVP realizado como avaliaçao do Campinas Tech Talents da trilha de Python oferecido pela Enforce

# Como rodar o projeto.

<ol>
  <h2><i>Banco de dados</i></h2>
  <li> Neste projeto, adicionamos na pasta <i>Database</i> um script que caso prefira, pode rodar dentro do seu banco <i>PostgreSQL.</i></li>
  <li>As tabelas são criadas dentro do <i>Backend</i> pelo comando <i>db.create_all()</i></li>
</ol>

<ol>
  <h2><i>Backend</i></h2>
  <li>Entre na pasta do backend e utilieze o comando <i>set FLASK_APP=main.py</i></li>
  <li>Instale as dependencias com o comando <i>pip install -r requiriments.txt</i></li>
  <li>No terminal utilize o comando <i>flask run</i></li>
</ol>

<ol>
  <h2><i>FrontEnd</i></h2>
  <li>Entre na pasta do frontend e utilieze o comando <i>npm install</i> para instalar todos os modulos/dependencias</li>
  <li>No terminal utilize o comando ng serve --open</li>
</ol>



# TODO's
<ol>
  <h2><i>Banco de dados</i></h2>
  <li>Criação da tabela de endereços relacionado ao cliente e proprietario. <i>Um cliente/proprietario pode ter mais de um endereço.</i></li>
</ol>

<ol>
  <h2><i>FrontEnd</i></h2>
  <li>Melhorar o design das rotas.</li>
  <li>Adicionar <i>Compras,</i> <i>Gastos do imovel</i>, <i>Criaçao de Banco</i></li>
</ol>

<ol>
  <h2><i>Back-end</i></h2>
  <li>Melhorar o codigo em si, separando em pastas os objetos e diminuir o codigo no <i>main.py</i>.</li>
  <li>Importar o <i>Swagger</i> para um arquivo proprio e melhor documentado.</i></li>
</ol>
