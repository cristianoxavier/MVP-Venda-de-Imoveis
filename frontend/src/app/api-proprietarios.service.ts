import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiProprietariosService {

  public endpoint = 'http://127.0.0.1:5000';

  constructor(private httpClient: HttpClient) { }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  }

  /* ROTAS PROPRIETARIOS */

  public getAllProprietarios():Observable<any>{
    return this.httpClient.get(this.endpoint + '/mvp/proprietario')
  }

  public postProprietario(proprietario:any){
    return this.httpClient.post(this.endpoint + '/mvp/proprietario', proprietario);
  }

  public deleteProprietario(id_proprietario:number) {
    return this.httpClient.delete(this.endpoint + '/mvp/proprietario/' + id_proprietario)
  }
}
