import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  public endpoint = 'http://127.0.0.1:5000';

  constructor(private httpClient: HttpClient) { }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  }
  /*ROTAS CLIENTE*/
  public getAllClientes(): Observable<any>{
    return this.httpClient.get(this.endpoint + '/mvp/clientes');
  }

  public getClienteId(id_cliente: number): Observable<any>{
    let url = this.endpoint + `/mvp/clientes/${id_cliente}`
    console.log(url)
    return this.httpClient.get(url)

  }

  public postCliente(cliente:any){
    return this.httpClient.post(this.endpoint + '/mvp/clientes', cliente);
  }

  public deleteCliente(id_cliente:number) {
    return this.httpClient.delete(this.endpoint + `/mvp/clientes/` + id_cliente)
  }

}

