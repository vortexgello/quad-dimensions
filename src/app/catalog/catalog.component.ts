import { Component } from '@angular/core';
import * as catalog from './catalog.json'

@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html',
  styles: [
  ]
})
export class CatalogComponent {
  catalog: any[] = (catalog as any).default
}