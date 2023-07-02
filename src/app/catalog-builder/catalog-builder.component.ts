import { Component } from '@angular/core';

@Component({
  selector: 'app-catalog-builder',
  templateUrl: './catalog-builder.component.html',
  styles: [
  ]
})
export class CatalogBuilderComponent {

  addCategoryPopup = false
  selectedCategoryIndex = 0
  addProductPopup = false
  editProductPopup = false
  selectedProductIndex = 0

  categoryTitle = ''
  product = {
    title: '',
    img: '',
    bool: false,
    pdf: '',
    types: {
      type1_title: '',
      pdf1:'',
      type2_title: '',
      pdf2: ''
    }
  }

  jsonData = JSON.parse(localStorage.getItem("data") as string) || JSON.parse("[]")

  addCategory = () => {
    this.jsonData.push({
      "title": this.categoryTitle,
      "products": []
    })
    this.addCategoryPopup = false
    this.updateLocalStorage()
  }

  addProduct = (index: number) => {
    this.jsonData[index].products.push({
      "title": this.product.title,
      "image": this.product.img,
      "pdf": this.product.bool ? null : this.product.pdf,
      "types": !this.product.bool ? null : [
        {
          "title":this.product.types.type1_title,
          "pdf": this.product.types.pdf1
        },
        {
          "title":this.product.types.type2_title,
          "pdf": this.product.types.pdf2
        },
      ]
    })
    this.addProductPopup = false
    this.updateLocalStorage()
  }

  resetProduct = () => {
    this.product = {
      title: '',
      img: '',
      bool: false,
      pdf: '',
      types: {
        type1_title: '',
        pdf1:'',
        type2_title: '',
        pdf2: ''
      }
    }
  }

  updateLocalStorage = () => {
    localStorage.setItem("data", JSON.stringify(this.jsonData))
  }

  copy2clip = () => {
    navigator.clipboard.writeText(JSON.stringify(this.jsonData))
  }

}
