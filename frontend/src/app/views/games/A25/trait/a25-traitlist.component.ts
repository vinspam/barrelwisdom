import { Dialog } from '@angular/cdk/dialog';
import { Location } from '@angular/common';
import { Component } from '@angular/core';
import { UntypedFormBuilder } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { BreadcrumbService } from '@app/services/breadcrumb.service';
import { DestroyService } from '@app/services/destroy.service';
import { SeoService } from '@app/services/seo.service';
import { FilterListComponent } from '@app/views/_components/filter-list/filter-list.component';
import { Trait } from '@app/views/games/A25/_services/a25.interface';
import { A25Service } from '@app/views/games/A25/_services/a25.service';
import { CommonImports, MaterialFormImports } from '@app/views/games/_prototype/SharedModules/common-imports';
import { DialogUseComponent } from '@app/views/games/_prototype/dialog-use.component';
import { Observable, forkJoin } from 'rxjs';
import { map, startWith } from 'rxjs/operators';
import { A25CharaComponent } from '../character/a25-chara.component';
import { A25ItemComponent } from '../item/a25-item.component';
import { A25TraitComponent } from './a25-trait.component';

@Component({
  templateUrl: 'a25-traitlist.component.html',
  providers: [DestroyService],
  standalone: true,
  imports: [...CommonImports, ...MaterialFormImports,
    A25ItemComponent, A25TraitComponent, A25CharaComponent, FilterListComponent]
})

export class A25TraitlistComponent extends DialogUseComponent {
  filteredTraits: Observable<Trait[]>;
  c2;
  c3;

  constructor(
    protected cdkDialog: Dialog,
    protected readonly destroy$: DestroyService,
    protected router: Router,
    protected route: ActivatedRoute,
    protected location: Location,
    protected seoService: SeoService,
    protected breadcrumbService: BreadcrumbService,
    private formBuilder: UntypedFormBuilder,
    protected a25service: A25Service,) {
    super(destroy$, router, route, location, seoService, breadcrumbService, cdkDialog);
    this.component = A25TraitComponent;
    this.c2 = A25CharaComponent;
    this.c3 = A25ItemComponent;
    this.pageForm = this.formBuilder.group({
      filtertext: '',
      transfers: "any"
    })
  }

  changeData() {
    this.gameService(this.a25service, 'traits');
    this.genericSettings(`Traits`, `The list of traits in ${this.gameTitle}.`);
    this.pageForm.reset();
    return forkJoin({
      traits: this.a25service.getTraitList(this.language),
      transfer: this.a25service.getFilter("combat_type", this.language),
    })
  }

  afterAssignment(): void {
    this.filteredTraits = this.pageForm.valueChanges.pipe(
      startWith(null as Observable<Trait[]>),
      map((search: any) => search ? this.filterT(search.filtertext, search.transfers) : this.data.traits.slice())
    );
  }

  extraSettings(): void {
    this.dialogref.componentInstance.itemkind = 'materials'
  }

  private filterT(value: string, transfer: string): Trait[] {
    this.hide = false;
    let traitlist: Trait[] = this.data.traits;

    switch (transfer) {
      case "attack":
        traitlist = traitlist.filter(trait => trait.trans_atk);
        break;
      case "healing":
        traitlist = traitlist.filter(trait => trait.trans_heal);
        break;
      case "buff":
        traitlist = traitlist.filter(trait => trait.trans_buff);
        break;
      case "debuff":
        traitlist = traitlist.filter(trait => trait.trans_dbf);
        break;
      case "equipment":
        traitlist = traitlist.filter(trait => trait.trans_wep);
        break;
    }
    if (!value) {
      return traitlist;
    }
    const filterValue = value.toLowerCase();
    return traitlist.filter(trait => {
      return trait.name.toLowerCase().includes(filterValue) ||
        trait.desc.toLowerCase().includes(filterValue)
    });
  }
}