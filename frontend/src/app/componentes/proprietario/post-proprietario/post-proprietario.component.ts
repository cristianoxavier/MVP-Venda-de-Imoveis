import { Component, OnInit } from '@angular/core';
import { ApiProprietariosService } from '../../../api-proprietarios.service';

@Component({
  selector: 'app-post-proprietario',
  templateUrl: './post-proprietario.component.html',
  styleUrls: ['./post-proprietario.component.scss']
})
export class PostProprietarioComponent implements OnInit {

  

  constructor(private apiProprietariosService: ApiProprietariosService) { }

  ngOnInit(): void {
  }

  addNewProprietario(nm_proprietario:string, cpf_proprietario:string, rg_proprietario:string, data_nascimento:string, estado_civil:string, profissao:string){
    this.apiProprietariosService.postProprietario({"nm_proprietario":nm_proprietario , "cpf_proprietario":cpf_proprietario, "rg_proprietario":rg_proprietario, "data_nascimento":data_nascimento, "estado_civil":estado_civil, "profissao":profissao}).subscribe(data => {
      console.log(data)
    }, error => {
      console.log("Error", error)
    }
  )}
}
