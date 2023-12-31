import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { CatalogComponent } from './catalog/catalog.component';
import { ViewerComponent } from './viewer/viewer.component';
import { ContactComponent } from './contact/contact.component';
import { CatalogBuilderComponent } from './catalog-builder/catalog-builder.component';

const routes: Routes = [
  {
    path: '', redirectTo: 'home', pathMatch: 'full'
  },
  {
    path: 'home', component: HomeComponent
  },
  {
    path: 'catalog', component: CatalogComponent,
  },
  {
    path: 'pdfs/:id', component: ViewerComponent,
  },
  {
    path: 'contact', component: ContactComponent,
  },
  {
    path: 'builder', component: CatalogBuilderComponent
  }
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
