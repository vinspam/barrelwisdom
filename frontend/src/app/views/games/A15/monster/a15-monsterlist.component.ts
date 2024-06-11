import { Dialog } from '@angular/cdk/dialog';
import { Location } from '@angular/common';
import { Component } from '@angular/core';
import { UntypedFormBuilder } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { ActivatedRoute, Router } from '@angular/router';
import { DestroyService } from '@app/services/destroy.service';
import { SeoService } from '@app/services/seo.service';
import { MonsterList } from '@app/views/games/A15/_services/a15.interface';
import { A15Service } from '@app/views/games/A15/_services/a15.service';
import { CommonImports, MaterialFormImports } from '@app/views/games/_prototype/SharedModules/common-imports';
import { DialogUseComponent } from '@app/views/games/_prototype/dialog-use.component';
import { Observable } from 'rxjs';
import { map, startWith } from 'rxjs/operators';
import { A15MonsterComponent } from './a15-monster.component';

@Component({
  templateUrl: 'a15-monsterlist.component.html',
  providers: [DestroyService],
  standalone: true,
  imports: [...CommonImports, ...MaterialFormImports,
    A15MonsterComponent, MatButtonModule]
})

export class A15MonsterlistComponent extends DialogUseComponent {
  filteredMonsters: Observable<MonsterList[]>;

  constructor(
    protected cdkDialog: Dialog,
    protected readonly destroy$: DestroyService,
    protected router: Router,
    protected route: ActivatedRoute,
    protected location: Location,
    protected seoService: SeoService,
    private formBuilder: UntypedFormBuilder,
    private a15service: A15Service) {
    super(destroy$, router, route, location, seoService, cdkDialog);
    this.component = A15MonsterComponent;
    this.pageForm = this.formBuilder.nonNullable.group({
      filtertext: '',
    })
  }

  changeData() {
    this.gameService(this.a15service, 'monsters');
    this.genericSEO(`Monsters`, `The list of monsters in ${this.gameTitle}.`);
    this.pageForm.reset();
    return this.a15service.getMonsterList(this.language);
  }

  afterAssignment(): void {
    this.filteredMonsters = this.pageForm.valueChanges.pipe(
      startWith(null as Observable<MonsterList[]>),
      map((search: any) => search ? this.filterT(search.filtertext) : this.data.slice())
    );
  }

  private filterT(value: string): MonsterList[] {
    let list: MonsterList[] = this.data;
    if (!value) {
      return list;
    }
    const filterValue = value.toLowerCase();
    return list.filter(mon => {
      return mon.name.toLowerCase().includes(filterValue);
    });
  }
}