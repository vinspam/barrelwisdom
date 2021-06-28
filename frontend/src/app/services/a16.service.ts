import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders,  } from '@angular/common/http';
import { Observable} from 'rxjs';
import { environment } from '@environments/environment';
import { Property, AreaData, Effect, MonsterList, MonsterFull, Book, ItemList, ItemFull, Category, CategoryData } from '@app/interfaces/a16';

@Injectable({ providedIn: 'root' })
export class A16Service {
    httpOptions = {
        headers: new HttpHeaders({ 'Content-Type': 'application/json' })
      };
    
    constructor(
      private http: HttpClient,
    ) { }

    public readonly gameTitle = "Atelier Shallie";
    public readonly gameURL = "shallie";
    public readonly imgURL = `${environment.mediaURL}games/${this.gameURL}/`;
    
    getPropertyList(language: string): Observable<Property[]> {
      return this.http.get<Property[]>(`${environment.apiUrl}/A16/property/${language}/`);
    }

    getProperty(slugname: string, language: string): Observable<Property> {
      return this.http.get<Property>(`${environment.apiUrl}/A16/property/${slugname}/${language}/`);
    }

    getEffectList(language: string): Observable<Effect[]> {
      return this.http.get<Effect[]>(`${environment.apiUrl}/A16/effect/${language}/`);
    }

    getEffect(slugname: string, language: string): Observable<Effect> {
      return this.http.get<Effect>(`${environment.apiUrl}/A16/effect/${slugname}/${language}/`);
    }

    getMonsterList(language: string): Observable<MonsterList[]> {
      return this.http.get<MonsterList[]>(`${environment.apiUrl}/A16/monster/${language}/`);
    }

    getMonster(slugname: string, language: string): Observable<MonsterFull> {
      return this.http.get<MonsterFull>(`${environment.apiUrl}/A16/monster/${slugname}/${language}/`);
    }

    getBookList(language: string): Observable<Book[]> {
      return this.http.get<Book[]>(`${environment.apiUrl}/A16/book/${language}/`);
    }

    getBook(slugname: string, language: string): Observable<Book> {
      return this.http.get<Book>(`${environment.apiUrl}/A16/book/${slugname}/${language}/`);
    }

    getItemList(language: string): Observable<ItemList[]> {
      return this.http.get<ItemList[]>(`${environment.apiUrl}/A16/item/${language}/`);
    }

    getItem(slugname: string, language: string): Observable<ItemFull> {
      return this.http.get<ItemFull>(`${environment.apiUrl}/A16/item/${slugname}/${language}/`);
    }

    getCategories(language: string): Observable<Category[]> {
      return this.http.get<Category[]>(`${environment.apiUrl}/A16/category/${language}/`);
    }

    getCategory(slugname: string, language: string): Observable<CategoryData> {
      return this.http.get<CategoryData>(`${environment.apiUrl}/A16/category/${slugname}/${language}/`);
    }

    getRegion(slugname: string, language: string): Observable<AreaData> {
      return this.http.get<AreaData>(`${environment.apiUrl}/A16/area/${slugname}/${language}/`);
    }
    
}