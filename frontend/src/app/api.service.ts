import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  public endpoint = 'http://127.0.0.1:5000';

  constructor(private httpClient: HttpClient) { }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  }

  public getAllClientes(): Observable<any>{
    return this.httpClient.get(this.endpoint + '/clientes/v1/clientes');
  }

  public getClienteId(id_cliente: number): Observable<any>{
    return this.httpClient.get(this.endpoint + `/clientes/v1/clientes/` + id_cliente)
  }

  public postCliente(cliente:any){
    return this.httpClient.post(this.endpoint + '/clientes/v1/clientes', cliente);
  }

  public deleteCliente(id_cliente:number) {
    return this.httpClient.delete(this.endpoint + `/clientes/v1/clientes/` + id_cliente)
  }


}

