import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-viewer',
  templateUrl: './viewer.component.html',
  styles: [
  ]
})
export class ViewerComponent {
  constructor(private route: ActivatedRoute) {}
  id = this.route.snapshot.paramMap.get('id')
}
