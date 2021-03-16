import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { GetAllClientesComponent } from './componentes/cliente/get-all-clientes/get-all-clientes.component';
import { GetClienteComponent } from './componentes/cliente/get-cliente/get-cliente.component';
import { PostClienteComponent } from './componentes/cliente/post-cliente/post-cliente.component';



const routes: Routes = [
  {path:'getallclientes', component: GetAllClientesComponent},
  {path:'addcliente', component: PostClienteComponent},
  {path:'getclienteid', component: GetClienteComponent}

]
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
