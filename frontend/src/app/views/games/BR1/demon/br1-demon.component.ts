import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Demon } from '@app/interfaces/br1';
import { BR1Service } from '@app/services/br1.service';
import { SeoService } from '@app/services/seo.service';

@Component({
  templateUrl: 'br1-demon.component.html',
  selector: 'br1-demon',
})
export class BR1DemonComponent implements OnInit {

  loading = false;
  submitted = false;
  returnUrl: string;
  error: string = '';
  demon: Demon;
  colset: string;

  seoTitle: string;
  seoDesc: string;
  seoImage: string;
  seoURL: string;

  gameTitle: string;
  gameURL: string;
  imgURL: string;

  @Input()
  slugname: string = "";

  @Input()
  showNav: boolean = true;

  language = "";

constructor(
    private route: ActivatedRoute,
    private br1service: BR1Service,
    private seoService: SeoService) {
      if(this.route.snapshot.params.demon != null) {
      this.slugname = this.route.snapshot.params.demon;
    }
  }
  ngOnInit(): void {
    this.language = this.route.snapshot.params.language;
    if(this.showNav) {
      this.colset = "col-md-7 mx-auto "
    }
    this.br1service.getDemon(this.slugname, this.language)
    .subscribe({next: demon => {
        this.error =``;
        this.demon = demon;

        this.gameTitle = this.br1service.gameTitle;
        this.gameURL = this.br1service.gameURL;
        this.imgURL = this.br1service.imgURL;

        this.seoURL = `${this.gameURL}/demons/${this.demon.slugname}/${this.language}`;
        this.seoTitle = `${this.demon.name} - ${this.gameTitle}`;
        this.seoDesc = `${this.demon.flavor}`
        this.seoService.SEOSettings(this.seoURL, this.seoTitle, this.seoDesc, this.seoImage);
    },
    error: error => {
      this.error =`${error.status}`;
      
    }});
  }
} 