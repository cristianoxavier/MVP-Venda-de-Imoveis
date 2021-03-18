# MVP-Venda-de-Imoveis
Um projeto MVP realizado como avaliaçao do <i>Campinas Tech Talents - 2021</i> da trilha de <i>Python</i> oferecido pela <i>Enforce</i>.

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



## ⚙️ Known Issues

- Sistema CRUD não implementado completamente no Front-End;
- Criação da tabela de endereços relacionado ao cliente e proprietario. <i>Um cliente/proprietario pode ter mais de um endereço.;



## 🛠️ Construído com

* [Angular](https://angular.io/) - O framework web usado.
* [Bootstrap](https://getbootstrap.com/) - O framework de estilos usado.
* [SQLAlchemy](https://www.sqlalchemy.org/) - Estruturação do banco de dados.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Usada para gerar os microsserviços.
* [PostgreSQL](https://www.postgresql.org/) - Armazenamento dos dados.


## ✒️ Autor

* **Cristiano Xavier** - *Responsável por estruturar o banco de dados no Postgre, codificar o backend e desenvolver o Front-End*
* [GitHub](https://github.com/cristianoxavier) 
* [Linkedin](https://www.linkedin.com/in/cristiano-xavier-2021/)
