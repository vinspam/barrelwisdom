import { Component, OnInit, TemplateRef } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BsModalService, BsModalRef, ModalOptions } from 'ngx-bootstrap/modal';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { Location } from '@angular/common';
import { Item, Name } from '@app/interfaces/a22';
import { A22Service } from '@app/services/a22.service';
import { ErrorCodeService } from "@app/services/errorcode.service";
import { Observable } from 'rxjs';
import { map, startWith } from 'rxjs/operators';
import { SeoService } from '@app/services/seo.service';
import { Meta, Title } from '@angular/platform-browser';

@Component({
    templateUrl: 'a22-itemlist.component.html',
    selector: 'a22-itemlist',
  })

  export class A22ItemlistComponent implements OnInit {
    modalRef: BsModalRef;
    pageForm: FormGroup;
    itemControl: FormControl;
    ingControl: FormControl;
    error: boolean = false;
    errorCode: string;
    errorVars: any[];
    errorMsg: string;
    item: string = "items";
    items: Item[];
    filteredItems: Observable<Item[]>;
    currentType: string = "Any";
    currentElem: string = "Any";
    currentElemVal: number = 1;
    searchstring = "";
    ingstring = "";
    language = "";
    config: ModalOptions = { class: "col-md-5 mx-auto" };
    categories: Name[];
    selectedCat = "Any";
    selectedElem = "Any";
    selectedElemV = 0;
  
    constructor(
      private modalService: BsModalService,
      private formBuilder: FormBuilder,
      private route: ActivatedRoute,
      private location: Location,
      private a22service: A22Service,
      private errorService: ErrorCodeService,
      private seoService: SeoService,
      private metaService: Meta,
      private titleService: Title
    ) { 
      this.itemControl = new FormControl();
      this.ingControl = new FormControl();
    }
  
    ngOnInit(): void {
  
      this.language = this.route.snapshot.params.language;
  
      this.getItems();
      this.getCategories();
      this.seoService.createCanonicalURL(`ryza2/items/${this.language}`);
      this.titleService.setTitle(`Items - Atelier Ryza 2 - Barrel Wisdom`);
      this.metaService.updateTag({ name: `robots`, content: `index, archive` },`name="robots"`);
      this.metaService.updateTag({ name: `description`, content: `The list of items in Atelier Ryza 2.` }, `name="description"`);
      this.metaService.updateTag({ property: `og:title`, content: `Items` }, `property="og:title"`);
      this.metaService.updateTag({ property: `og:description`, content: `The list of items in Atelier Ryza 2.` },`property="og:description"`);
      this.metaService.updateTag({ property: `og:type`, content: `webpage` }, `property="og:type"`);
      this.metaService.updateTag({ property: `og:image`, content: `/media/main/barrel.png` }, `property="og:image"`);
  
      this.pageForm = this.formBuilder.group({
        filtertext: this.itemControl,
        filtering: this.ingControl,
        type: ['Any'],
        elementval: [1],
        element: ["Any"]
      })
  
      this.pageForm.get('type').valueChanges
        .subscribe(type => {
          this.currentType = type;
        });

        this.pageForm.get('elementval').valueChanges
        .subscribe(val => {
          this.currentElemVal = val;
        });

        this.pageForm.get('element').valueChanges
        .subscribe(val => {
          this.currentElem = val;
        });
  
      this.itemControl.valueChanges.subscribe(search => {
        this.searchstring = search;
      });

      this.ingControl.valueChanges.subscribe(search => {
        this.ingstring = search;
      });
    }
  
    getItems() {
      this.a22service.getItemList(this.language)
      .subscribe(items => {
        this.items = items;
        this.filteredItems = this.pageForm.valueChanges.pipe(
          startWith(null as Observable<Item[]>),
          map((search: string | null) => search ? this.filterT(this.searchstring, this.currentType, this.currentElemVal, this.currentElem, this.ingstring) : this.items.slice())
        );
      },
      error => {
        this.error = true,
        this.errorCode = error.status.toString(),
        this.errorVars = this.errorService.getCodes(this.errorCode)
      });
    }

    getCategories() {
        this.a22service.getCategoryList(this.language)
        .subscribe(categories  => {
            this.categories = categories;
        },
        error => {
            this.error = true,
            this.errorCode = error.status.toString(),
            this.errorVars = this.errorService.getCodes(this.errorCode)
        });
    }
  
    openModal(template: TemplateRef<any>, slugname: string) {
      this.item = slugname;
      this.location.go('ryza2/items/' + slugname + "/" + this.language);
      this.modalRef = this.modalService.show(template);
      this.modalRef.onHide.subscribe((reason: string | any) => {
          this.location.go('ryza2/items/' + this.language);
        })
    }
  
    private filterT(value: string, type: string, elementV: number, element: string, ing: string): Item[] {
  
      const filterValue = value.toLowerCase();
      let list: Item[] = this.items;

      if(type != 'Any') {
          list = list.filter(item => item.category.some(c => c.name == type) );
      }

      if(elementV > 1) {
          list = list.filter(item => item.elementvalue >= elementV);
      }

      switch(element) {
          case "Fire": {
              list = list.filter(item => item.fire)
              break;
          }
          case "Ice": {
            list = list.filter(item => item.ice)
            break;
          }
          case "Lightning": {
              list = list.filter(item => item.lightning)
              break;
          }
          case "Wind": {
              list = list.filter(item => item.wind)
              break;
          }
      }

      if(ing.length > 0) {
          list = list.filter(item => (item.ingredient_set) ? item.ingredient_set.some(i => (i.item) ? i.item.toLowerCase().includes(ing) : i.category.toLowerCase().includes(ing)) : false)
      }

      if(value.length > 0) {
        list = list.filter(item => { 
            return item.name.toLowerCase().includes(filterValue);
          });
      }

      return list;
    } 
  
    get f() { return this.pageForm.controls; }
  
  }