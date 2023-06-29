import { Component } from '@angular/core';
import * as catalog from '../../assets/catalog.json'

@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html',
  styles: [
  ]
})
export class CatalogComponent {
  catalog: any[] = (catalog as any).default
}