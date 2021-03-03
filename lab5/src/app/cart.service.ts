import { Injectable } from '@angular/core';
// import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CartService {
  items = [];
  constructor(
    // private http: HttpClient
  ) {}


  // tslint:disable-next-line:typedef
  addToCart(product: any) {

  }

  // tslint:disable-next-line:typedef
  getItems() {

  }

  // tslint:disable-next-line:typedef
  clearCart() {

  }
}
