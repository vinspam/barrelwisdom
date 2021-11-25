import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';

import { BRSLFragmentComponent } from './brsl-fragmentlist.component';
import { BRSLFragmentRoutingModule } from './brsl-fragment-routing.module';
import { LanguageModule } from '@app/views/language/language.module';
import { PipeModule } from '@app/pipes/pipes.module';
import { ErrorModule } from '@app/views/error/error.module';

import {MatInputModule} from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatChipsModule } from '@angular/material/chips';
import {MatAutocompleteModule} from '@angular/material/autocomplete';
import {OverlayModule} from '@angular/cdk/overlay'; 
import {MatIconModule} from '@angular/material/icon'; 
import {MatSelectModule} from '@angular/material/select';
import {MatButtonModule} from '@angular/material/button';
import { PopoverModule } from 'ngx-bootstrap/popover';

@NgModule({
    imports: [
      CommonModule,
      FormsModule,
      ReactiveFormsModule,
      BRSLFragmentRoutingModule,
      PipeModule,
      MatInputModule,
      MatFormFieldModule,
      MatChipsModule,
      MatAutocompleteModule,
      OverlayModule,
      MatIconModule,
      MatSelectModule,
      MatButtonModule,
      LanguageModule,
      ErrorModule,
      PopoverModule.forRoot()
    ],
    declarations: [
        BRSLFragmentComponent,    ],
    exports: [
        BRSLFragmentComponent,    ],
  })
  export class BRSLFragmentModule {}