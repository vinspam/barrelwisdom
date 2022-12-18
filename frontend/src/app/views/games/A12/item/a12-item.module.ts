import { NgModule } from '@angular/core';
import { MatLegacyButtonModule as MatButtonModule } from '@angular/material/legacy-button';
import { MatIconModule } from '@angular/material/icon';
import { MatLegacySelectModule as MatSelectModule } from '@angular/material/legacy-select';
import { ErrorModule } from '@app/views/error/error.module';
import { SharedModule } from '@app/views/games/_prototype/SharedModules/shared.module';
import { A12ItemRoutingModule } from './a12-item-routing.module';
import { A12ItemComponent } from './a12-item.component';
import { A12ItemlistComponent } from './a12-itemlist.component';

@NgModule({
    imports: [
      SharedModule,
      A12ItemRoutingModule,
      MatIconModule,
      MatSelectModule,
      MatButtonModule,
      ErrorModule,
    ],
    declarations: [
        A12ItemlistComponent,
        A12ItemComponent,
    ]
  })
  export class A12ItemModule {}