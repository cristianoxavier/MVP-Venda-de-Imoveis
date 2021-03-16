import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../api.service';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-get-all-clientes',
  templateUrl: './get-all-clientes.component.html',
  styleUrls: ['./get-all-clientes.component.scss']
})
export class GetAllClientesComponent implements OnInit {

  clientes;
  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getClientes();
  }

  getClientes() {
    this.apiService.getAllClientes().subscribe((data)=>{console.log(data);this.clientes = data});
  }

  deleteCliente(id_cliente) {
    this.apiService.deleteCliente(id_cliente).subscribe(() => {
      this.getClientes();
    });
  }

}
