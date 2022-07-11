import { Location } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { UntypedFormBuilder, UntypedFormControl } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { DestroyService } from '@app/services/destroy.service';
import { SeoService } from '@app/services/seo.service';
import { Book } from '@app/views/games/A16/_services/a16.interface';
import { A16Service } from '@app/views/games/A16/_services/a16.service';
import { ListComponent } from '@app/views/games/_prototype/list.component';
import { BsModalService } from 'ngx-bootstrap/modal';
import { Observable } from 'rxjs';
import { map, startWith, takeUntil } from 'rxjs/operators';

@Component({
  templateUrl: 'a16-booklist.component.html',
  providers: [DestroyService]
})

export class A16BooklistComponent extends ListComponent implements OnInit {
  bookControl: UntypedFormControl;
  books: Book[];
  filteredBooks: Observable<Book[]>;

  constructor(
    protected modalService: BsModalService,
    protected readonly destroy$: DestroyService,
    protected router: Router,
    protected route: ActivatedRoute,
    protected location: Location,
    protected seoService: SeoService,
    private formBuilder: UntypedFormBuilder,
    private a16service: A16Service,
  ) {
    super(modalService, destroy$, router, route, location, seoService);
    this.gameService(this.a16service, 'recipe-books');
    this.bookControl = new UntypedFormControl();
    this.pageForm = this.formBuilder.group({
      filtertext: this.bookControl,
    })
  }

  ngOnInit(): void {
    this.modalEvent();
    this.getBooks();
    this.genericSEO(`Recipe Books`, `The list of recipe books in ${this.gameTitle}.`);
  }

  getBooks() {
    this.a16service.getBookList(this.language)
      .pipe(takeUntil(this.destroy$))
      .subscribe({
        next: books => {
          this.books = books;
          this.filteredBooks = this.pageForm.valueChanges.pipe(
            startWith(null as Observable<Book[]>),
            map((search: any) => search ? this.filterT(search.filtertext) : this.books.slice())
          );
        },
        error: error => {
          this.error = `${error.status}`;
        }
      });
  }

  private filterT(value: string): Book[] {
    let list: Book[] = this.books;
    if (!value) {
      return list;
    }
    const filterValue = value.toLowerCase();
    return list.filter(book => {
      return book.name.toLowerCase().includes(filterValue);
    });
  }

  identify2(index, item) {
    return item.slugname;
  }
}