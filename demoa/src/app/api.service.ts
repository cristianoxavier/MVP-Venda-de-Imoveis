import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  public host = 'http://127.0.0.1:5000/clientes/v1/clientes';

  constructor(private httpClient: HttpClient) { }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  }

  public getClientes(): Observable<any>{
    return this.httpClient.get('http://127.0.0.1:5000/clientes/v1/clientes');
  }

}


