import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiImoveisService {

  public endpoint = 'http://127.0.0.1:5000';

  constructor(private httpClient: HttpClient) { }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  }

  /*ROTAS IMOVEIS*/
  public getAllImoveis(): Observable<any>{
    return this.httpClient.get(this.endpoint + '/mvp/imoveis');
  }

  public postImovel(imovel:any){
    return this.httpClient.post(this.endpoint + '/mvp/imoveis', imovel);
  }

  public deteleImovel(id_imovel:number) {
    return this.httpClient.delete(this.endpoint + '/mvp/imoveis/' + id_imovel)
  }
}
