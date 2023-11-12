import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { UserProfile } from '@app/interfaces/user';
import { DestroyService } from '@app/services/destroy.service';
import { UserService } from '@app/services/user.service';
import { takeUntil } from 'rxjs';

@Component({
  templateUrl: 'user.component.html',
  providers: [DestroyService]
})

export class UserComponent implements OnInit {
  userprofile: UserProfile;
  error: string = '';
  errorVars: any[];

  constructor(
    private readonly destroy$: DestroyService,
    private route: ActivatedRoute,
    private userService: UserService,

  ) { }

  ngOnInit(): void {
    this.userService.getUserProfile(this.route.snapshot.params.username)
      .pipe(takeUntil(this.destroy$))
      .subscribe({
        next: x => {
          this.userprofile = x
        },
        error: error => {
          this.error = `${error.status}`;
        }
      });
  }
}