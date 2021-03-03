import { Component } from '@angular/core';

import { products } from '../products';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {
  products = products;

  // tslint:disable-next-line:typedef variable-name
  toggleCategory(category_id: string | number){
    // @ts-ignore
    products[category_id].toggle = !products[category_id].toggle;
  }

  // tslint:disable-next-line:typedef variable-name
  likeItem(category_id: string | number, item_id: string | number){
    // @ts-ignore
    products[category_id].items[item_id].likes+=1;
  }

  // tslint:disable-next-line:typedef variable-name
  removeItem(category_id: string | number, item_id: number){
    // @ts-ignore
    products[category_id].items.splice(item_id, 1);
    // @ts-ignore
    for (let i = item_id; i < products[category_id].items.length; i++) {
      // @ts-ignore
      products[category_id].items[i].id = i;
    }
  }

  // tslint:disable-next-line:typedef
  share() {
    window.alert('The product has been shared!');
  }
  // tslint:disable-next-line:typedef
  onNotify(){
    window.alert('You will be notified when the product goes on sale');
  }
}


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/
