import { Component, OnInit } from '@angular/core';
import { ApiImoveisService } from '../../../api-imoveis.service';

@Component({
  selector: 'app-get-all-imovel',
  templateUrl: './get-all-imovel.component.html',
  styleUrls: ['./get-all-imovel.component.scss']
})
export class GetAllImovelComponent implements OnInit {
  imoveis;
  constructor(private apiImoveisService: ApiImoveisService) { }

  ngOnInit(): void {
    this.getImoveis();
  }

  getImoveis(){
    this.apiImoveisService.getAllImoveis().subscribe({
      next: (data)=> {
        console.log(data);
        this.imoveis =data;
      },
      error: (error) => { console.log("Error", error)
    }})
  }

  deleteThisImovel(id_imovel:number){
    this.apiImoveisService.deteleImovel(id_imovel).subscribe(() => {
      this.getImoveis();
    });
  }

}
