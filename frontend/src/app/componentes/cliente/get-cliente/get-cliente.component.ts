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

  constructor(private apiService: ApiService, private ActivatedRoute: ActivatedRoute) {
    this.ActivatedRoute.queryParams.subscribe(params => {
      this.getClienteId(Number(params['id_cliente']))
    })
  }

  ngOnInit(): void {
  }

  getClienteId(id_cliente:number){
    this.apiService.getClienteId(id_cliente).subscribe(data =>{ this.cliente = data[id_cliente]; }, error => { console.log("Error", error) });
  }


}
