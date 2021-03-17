import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { GetAllClientesComponent } from './componentes/cliente/get-all-clientes/get-all-clientes.component';
import { GetClienteComponent } from './componentes/cliente/get-cliente/get-cliente.component';
import { PostClienteComponent } from './componentes/cliente/post-cliente/post-cliente.component';
import { GetAllImovelComponent } from './componentes/imovel/get-all-imovel/get-all-imovel.component';
import { PostImovelComponent } from './componentes/imovel/post-imovel/post-imovel.component';
import { GetAllProprietariosComponent } from './componentes/proprietario/get-all-proprietarios/get-all-proprietarios.component';
import { PostProprietarioComponent } from './componentes/proprietario/post-proprietario/post-proprietario.component';



const routes: Routes = [
  {path:'getallclientes', component: GetAllClientesComponent},
  {path:'addcliente', component: PostClienteComponent},
  {path:'getclienteid', component: GetClienteComponent},
  {path:'getallproprietarios', component: GetAllProprietariosComponent},
  {path:'addproprietario', component: PostProprietarioComponent},
  {path:'getallimoveis', component: GetAllImovelComponent},
  {path:'addimovel', component: PostImovelComponent}

]
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
