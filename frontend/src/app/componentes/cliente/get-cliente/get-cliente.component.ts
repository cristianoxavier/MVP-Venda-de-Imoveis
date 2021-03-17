import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../../../api.service';

@Component({
  selector: 'app-get-cliente',
  templateUrl: './get-cliente.component.html',
  styleUrls: ['./get-cliente.component.scss']
})
export class GetClienteComponent implements OnInit {
  cliente: any;
  clientes;

  constructor(private apiService: ApiService, private ActivatedRoute: ActivatedRoute) {
    /*this.ActivatedRoute.queryParams.subscribe(params => {
      this.getClienteId(Number(params['id_cliente']))
    })*/
  }

  ngOnInit() {
  }

  getClienteId(id_cliente:number) {

    console.log(id_cliente);
    this.apiService.getClienteId(id_cliente).subscribe({
      next: (cliente) => {
        this.cliente = cliente[id_cliente];
    },
      error: (error) => { console.log("Error", error) }
    });
  }


}
