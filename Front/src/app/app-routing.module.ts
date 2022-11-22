import { ProductComponent } from './product/product.component';
import { CreateAccountComponent } from './create-account/create-account.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { ShoppingCartComponent } from './shopping-cart/shopping-cart.component';

const routes: Routes = [
  {path: 'login', component: LoginComponent },
  {path: 'create-account', component: CreateAccountComponent},
  {path: 'product', component: ProductComponent},
  {path: 'shopping-cart' , component: ShoppingCartComponent}


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
