import { Dialog } from '@angular/cdk/dialog';
import { Location } from '@angular/common';
import { Component, ViewEncapsulation } from '@angular/core';
import { UntypedFormBuilder } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { ActivatedRoute, Router } from '@angular/router';
import { DestroyService } from '@app/services/destroy.service';
import { SeoService } from '@app/services/seo.service';
import { BreadcrumbService } from '@app/services/breadcrumb.service';
import { Item } from '@app/views/games/A25/_services/a25.interface';
import { A25Service } from '@app/views/games/A25/_services/a25.service';
import { CommonImports, MaterialFormImports } from '@app/views/games/_prototype/SharedModules/common-imports';
import { DialogUseComponent } from '@app/views/games/_prototype/dialog-use.component';
import { Observable, forkJoin } from 'rxjs';
import { map, startWith } from 'rxjs/operators';
import { A25IconComponent } from './a25-icon.component';
import { A25ItemComponent } from './a25-item.component';

@Component({
  templateUrl: 'a25-synthlist.component.html',
  styleUrls: ['../resleri.scss'],
  encapsulation: ViewEncapsulation.None,
  providers: [DestroyService],
  standalone: true,
  imports: [...CommonImports, ...MaterialFormImports,
    A25ItemComponent, A25IconComponent, MatButtonModule]
})

export class A25SynthesisListComponent extends DialogUseComponent {
  filteredItems: Observable<Item[]>;

  constructor(
    protected cdkDialog: Dialog,
    protected readonly destroy$: DestroyService,
    protected router: Router,
    protected route: ActivatedRoute,
    protected location: Location,
    protected seoService: SeoService,
    protected breadcrumbService: BreadcrumbService,
    private formBuilder: UntypedFormBuilder,
    protected a25service: A25Service) {
    super(destroy$, router, route, location, seoService, breadcrumbService, cdkDialog);
    this.component = A25ItemComponent;
    this.pageForm = this.formBuilder.nonNullable.group({
      filtertext: '',
      filtering: '',
      kind: 'Any',
      rarity: '0'
    })
  }

  changeData() {
    this.gameService(this.a25service, 'items/synthesis');
    this.genericSettings(`Synthesis Items`, `The list of synthesis items in ${this.gameTitle}.`);
    this.pageForm.reset();
    return forkJoin({
      items: this.a25service.getSynthList(this.language),
      equipment_type: this.a25service.getFilter('equipment', this.language),
      combat_type: this.a25service.getFilter('combat_type', this.language)
    })
  }

  afterAssignment(): void {
    this.filteredItems = this.pageForm.valueChanges.pipe(
      startWith(null as Observable<Item[]>),
      map((search: any) => search ? this.filterT(search.filtertext, search.kind, search.rarity, search.filtering) : this.data.items.slice())
    );
  }

  extraSettings(): void {
    this.dialogref.componentInstance.itemkind = 'synthesis'
  }

  replaceVal(item: Item): string {
    if (item.equip) {
      if (item.rarity === 4) {
        let desc = item.desc.replaceAll("{0}", `${item.equip[0].val_good / 100}`);
        if (item.equip[0].val2_good) desc = desc.replaceAll("{1}", `${item.equip[0].val2_good / 100}`);
        return desc;
      }
      if (item.equip[0].val_bad && !item.equip[0].val2_bad) {
        return item.desc.replaceAll("{0}", `${item.equip[0].val_bad / 100} ~ ${item.equip[0].val_good / 100}`)
      }
      if (item.equip[0].val2_bad) {
        return item.desc.replaceAll("{0}", `${item.equip[0].val_bad / 100} ~ ${item.equip[0].val_good / 100}`).replaceAll("{1}", `${item.equip[0].val2_bad / 100} ~ ${item.equip[0].val2_good / 100}`)
      }
      return item.desc.replaceAll("{0}", ` ${item.equip[0].val_good / 100}`).replaceAll("{1}", ` ${item.equip[0].val_good / 100}`)
    }
    if (item.combat) {
      if (item.combat[0].val_bad && !item.combat[0].val2_bad) {
        return item.desc.replaceAll("{0}", `${item.combat[0].val_bad / 100} ~ ${item.combat[0].val_good / 100}`)
      }
      if (item.combat[0].val2_bad) {
        return item.desc.replaceAll("{0}", `${item.combat[0].val_bad / 100} ~ ${item.combat[0].val_good / 100}`).replaceAll("{1}", `${item.combat[0].val2_bad / 100} ~ ${item.combat[0].val2_good / 100}`)
      }
      return item.desc.replaceAll("{0}", ` ${item.combat[0].val_good / 100}`).replaceAll("{1}", ` ${item.combat[0].val_good / 100}`)
    }
    return item.desc.replaceAll("{0}", ` ${item.combat[0].val_good / 100}`).replaceAll("{1}", ` ${item.combat[0].val_good / 100}`)
  }

  private filterT(value: string, kind: string, rarity: number, filter: string): Item[] {
    let list: Item[] = this.data.items;

    if (kind != 'Any') {
      list = list.filter(item => item.equip ? item.equip[0].kind == kind : item.combat[0].kind == kind);
    }
    if (rarity > 0) {
      list = list.filter(item => item.rarity == rarity)
    }
    if (filter) {
      filter = filter.toLowerCase()
      list = list.filter(item => item.ing ? item.ing.some(i => i.toLowerCase().includes(filter)) : false)
    }
    if (value) {
      const filterValue = (this.language == 'en') ? value.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, "") : value;
      list = list.filter(item => {
        return ((this.language == 'en') ?
          (item.name.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, "").includes(filterValue) || item.desc.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, "").includes(filterValue))
          : item.name.includes(filterValue) || item.desc.includes(filterValue));
      });
    }
    return list;
  }
}
