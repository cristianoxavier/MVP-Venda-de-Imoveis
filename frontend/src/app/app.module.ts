import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { GetAllClientesComponent } from './componentes/cliente/get-all-clientes/get-all-clientes.component';
import { PostClienteComponent } from './componentes/cliente/post-cliente/post-cliente.component';
import { GetClienteComponent } from './componentes/cliente/get-cliente/get-cliente.component';
import { GetAllProprietariosComponent } from './componentes/proprietario/get-all-proprietarios/get-all-proprietarios.component';
import { PostProprietarioComponent } from './componentes/proprietario/post-proprietario/post-proprietario.component';
import { GetAllImovelComponent } from './componentes/imovel/get-all-imovel/get-all-imovel.component';
import { PostImovelComponent } from './componentes/imovel/post-imovel/post-imovel.component';


@NgModule({
  declarations: [
    AppComponent,
    GetAllClientesComponent,
    PostClienteComponent,
    GetClienteComponent,
    GetAllProprietariosComponent,
    PostProprietarioComponent,
    GetAllImovelComponent,
    PostImovelComponent

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    NgbModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
