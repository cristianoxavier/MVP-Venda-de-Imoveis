import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-cliente',
  templateUrl: './cliente.component.html',
  styleUrls: ['./cliente.component.scss']
})
export class ClienteComponent implements OnInit {
  clientes;

  constructor(private apiService: ApiService) { }
  ngOnInit() {
    this.fetchClientes();
  }

  bntClientes(){
    this.fetchClientes;
  }

  fetchClientes() {
    this.apiService.getClientes()
    .subscribe(
      (data)=>{
        console.log(data);
        this.clientes = data;
    });
  }

}
