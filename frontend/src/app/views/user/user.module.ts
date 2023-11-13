import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { UserComponent } from './user.component';
import { UserRoutingModule } from './user-routing.module';
import { ErrorComponent } from '@app/views/error/error.component';

@NgModule({
    imports: [
      CommonModule,
      UserRoutingModule,
      ErrorComponent
    ],
    declarations: [
      UserComponent,
    ]
  })
  export class UserModule { }