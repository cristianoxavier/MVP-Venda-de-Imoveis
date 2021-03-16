import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../api.service';

@Component({
  selector: 'app-post-cliente',
  templateUrl: './post-cliente.component.html',
  styleUrls: ['./post-cliente.component.scss']
})
export class PostClienteComponent implements OnInit {

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }

  addNewClient(nm_cliente:string, cpf_cliente:string, rg_cliente:string, endereco:string, cep:string, uf:string, data_nascimento:string, estado_civil:string, profissao:string){
    this.apiService.postCliente({"nm_cliente":nm_cliente , "cpf_cliente":cpf_cliente, "rg_cliente":rg_cliente, "endereco":endereco, "cep":cep, "uf":uf, "data_nascimento":data_nascimento, "estado_civil":estado_civil, "profissao":profissao}).subscribe(data => {
      console.log(data)
    }, error => {
      console.log("Error", error)
    }
  )}
}


