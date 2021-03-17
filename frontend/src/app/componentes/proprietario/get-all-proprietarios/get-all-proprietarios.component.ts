import { Component, OnInit } from '@angular/core';
import { ApiProprietariosService } from '../../../api-proprietarios.service';

@Component({
  selector: 'app-get-all-proprietarios',
  templateUrl: './get-all-proprietarios.component.html',
  styleUrls: ['./get-all-proprietarios.component.scss']
})
export class GetAllProprietariosComponent implements OnInit {

  proprietarios;
  constructor(private apiProprietariosService: ApiProprietariosService) { }

  

  ngOnInit(): void {
    this.getProprietarios();
  }

  getProprietarios() {
    this.apiProprietariosService.getAllProprietarios().subscribe((data)=>{console.log(data);this.proprietarios = data});
  }

  deleteThisProprietario(id_proprietario: number) {
    this.apiProprietariosService.deleteProprietario(id_proprietario).subscribe(() => {
      this.getProprietarios();
    });
  }
}
