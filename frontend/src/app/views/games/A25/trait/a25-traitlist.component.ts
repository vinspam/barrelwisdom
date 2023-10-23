import { Location } from '@angular/common';
import { Component } from '@angular/core';
import { UntypedFormBuilder } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { DestroyService } from '@app/services/destroy.service';
import { SeoService } from '@app/services/seo.service';
import { NameLink, Trait } from '@app/views/games/A25/_services/a25.interface';
import { A25Service } from '@app/views/games/A25/_services/a25.service';
import { ModalUseComponent } from '@app/views/games/_prototype/modal-use.component';
import { BsModalService } from 'ngx-bootstrap/modal';
import { Observable } from 'rxjs';
import { map, startWith, takeUntil } from 'rxjs/operators';

@Component({
  templateUrl: 'a25-traitlist.component.html',
  providers: [DestroyService]
})

export class A25TraitlistComponent extends  ModalUseComponent {
  transfer: NameLink[];
  traits: Trait[];
  filteredTraits: Observable<Trait[]>;

  constructor(
    protected modalService: BsModalService,
    protected readonly destroy$: DestroyService,
    protected router: Router,
    protected route: ActivatedRoute,
    protected location: Location,
    protected seoService: SeoService,
    private formBuilder: UntypedFormBuilder,
    private a25service: A25Service,) {
    super(modalService, destroy$, router, route, location, seoService);
    this.pageForm = this.formBuilder.group({
      filtertext: '',
      transfers: "any"
    })
  }

  changeData(): void {
    this.pageForm.reset();
    this.getTransfer();
    this.getTraits();
  }

  getTraits() {
    this.a25service.getTraitList(this.language)
      .pipe(takeUntil(this.destroy$))
      .subscribe({
        next: traits => {
          this.traits = traits;
          this.gameService(this.a25service, 'traits');
          this.genericSEO(`Traits`, `The list of traits in ${this.gameTitle}.`);      
          this.filteredTraits = this.pageForm.valueChanges.pipe(
            startWith(null as Observable<Trait[]>),
            map((search: any) => search ? this.filterT(search.filtertext, search.transfers) : this.traits.slice())
          );
        },
        error: error => {
          this.error = `${error.status}`;
        }
      });
  }

  getTransfer() {
    this.a25service.getFilter("combat_type", this.language)
      .pipe(takeUntil(this.destroy$))
      .subscribe({
        next: transfer => {
          this.transfer = transfer;
        },
        error: error => {
          this.error = `${error.status}`;
        }
      });
  }

  private filterT(value: string, transfer: string): Trait[] {
    let traitlist: Trait[] = this.traits;

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
      return trait.name_en.toLowerCase().includes(filterValue) ||
        trait.name_ja.includes(filterValue) ||
        trait.desc.toLowerCase().includes(filterValue)
    });
  }
}