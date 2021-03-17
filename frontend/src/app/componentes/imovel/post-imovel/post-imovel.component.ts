import { Component, OnInit } from '@angular/core';
import { ApiImoveisService } from '../../../api-imoveis.service';

@Component({
  selector: 'app-post-imovel',
  templateUrl: './post-imovel.component.html',
  styleUrls: ['./post-imovel.component.scss']
})
export class PostImovelComponent implements OnInit {

  tipos_imoveis = ['APARTAMENTO',
  'CASA',
  'PREDIO COMERCIAL',
  'SITIO',
  'CHACARA',
  'TERRENO']

  ufs = ['AC',
  'AL',
  'AM',
  'AP',
  'BA',
  'CE',
  'DF',
  'ES',
  'GO',
  'MA',
  'MG',
  'MS',
  'MT',
  'PA',
  'PB',
  'PE',
  'PI',
  'PR',
  'RJ',
  'RN',
  'RO',
  'RR',
  'RS',
  'SC',
  'SE',
  'SP',
  'TO'
]
  constructor(private apiImoveisService: ApiImoveisService) { }

  ngOnInit(): void {
  }

  addNewImovel(tipo_imovel:string, endereco:string, complemento:string, cep:string, uf:string, id_proprietario:number, adquirido_em:string, valor_imovel:string){
    this.apiImoveisService.postImovel({"tipo_imovel":tipo_imovel , "endereco":endereco, "complemento":complemento, "cep":cep, "uf":uf, "id_proprietario":id_proprietario, "adquirido_em":adquirido_em, "valor_imovel":valor_imovel}).subscribe(data => {
      console.log(data)
    }, error => {
      console.log("Error", error)
    }
  )}

}
