import { Component, OnInit } from '@angular/core';
import { Input } from '@angular/core';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {
  @Input() product: any;
  constructor() { }

  // tslint:disable-next-line:typedef
  like(){

  }

  // tslint:disable-next-line:typedef
  ngOnInit() {
  }

}
