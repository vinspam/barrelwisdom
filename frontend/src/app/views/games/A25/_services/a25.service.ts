import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Character, Dungeon, Emblem, Item, Memoria, NameLink, RecipeTab, Research, ScoreBattle, Tower, Trait, Update } from '@app/views/games/A25/_services/a25.interface';
import { environment } from '@environments/environment';
import { Observable } from 'rxjs';


@Injectable({ providedIn: 'root' })
export class A25Service {
  private readonly version = '10-30-24';

  constructor(
    private http: HttpClient,
  ) { }

  public readonly gameTitle = {
    "en": "Atelier Resleriana",
    "ja": "レスレリアーナのアトリエ",
    "sc": "蕾斯莱莉娅娜的炼金工房",
    "tc": "蕾斯萊莉婭娜的鍊金工房"
  };
  public readonly gameURL = "resleri";
  public readonly imgURL = `${environment.mediaURL}games/${this.gameURL}/`;

  public readonly stats = {
    'hp': {
      "en": "HP", "ja": "HP", "sc": "HP", "tc": "HP"
    },
    'agi': {
      "en": "SPD", "ja": "素早い", "sc": "敏捷", "tc": "敏捷"
    },
    'patk': {
      "en": "PATK", "ja": "物攻", "sc": "物攻", "tc": "物攻"
    },
    'pdef': {
      "en": "PDEF", "ja": "物防", "sc": "物防", "tc": "物防"
    },
    'matk': {
      "en": "MATK", "ja": "魔攻", "sc": "魔攻", "tc": "魔攻"
    },
    'mdef': {
      "en": "MDEF", "ja": "魔防", "sc": "魔防", "tc": "魔防"
    },
    'date': {
      "en": "Date", "ja": "日付", "sc": "日期", "tc": "日期"
    },
  }

  public readonly colors = {
    'red':    '#b63c3c',
    'blue':   '#3883ad',
    'green':  '#3eb880',
    'yellow': '#c9af47',
    'purple': '#ac48b9'
  }

  public readonly colorList = {
    'red':    'rgba(182,60,60,.7);',
    'blue':   'rgba(56,131,173,0.7);',
    'green':  'rgba(62,184,128,0.7);',
    'yellow': 'rgba(201,175,71,0.7);',
    'purple': 'rgba(172,72,185,0.7);'
  }

  public readonly elements = {
    'wind': '#3b853d',
    'fire': '#b23e36',
    'ice': '#2089bc',
    'lightning': '#9e8a1a',
    'slash': '#776a55',
    'impact': '#72543b',
    'pierce': '#647189',
  }

  public readonly equipment = {
    "en":"Equipment",
    "ja":"装備",
    "sc":"装备",
    "tc":"裝備"
  }

  getFilter(slug: string, language: string): Observable<NameLink[]> {
    return this.http.get<NameLink[]>(`${environment.apiUrl}/A25/filterable/${slug}/${language}/?v=${this.version}`);
  }

  getTraitList(language: string): Observable<Trait[]> {
    return this.http.get<Trait[]>(`${environment.apiUrl}/A25/trait/${language}/?v=${this.version}`);
  }

  getTrait(slug: string, language: string): Observable<Trait> {
    return this.http.get<Trait>(`${environment.apiUrl}/A25/trait/${slug}/${language}/?v=${this.version}`);
  }

  getMaterialList(language: string): Observable<Item[]> {
    return this.http.get<Item[]>(`${environment.apiUrl}/A25/material/${language}/?v=${this.version}`);
  }

  getMaterial(slug: string, language: string): Observable<Item> {
    return this.http.get<Item>(`${environment.apiUrl}/A25/material/${slug}/${language}/?v=${this.version}`);
  }

  getSynthList(language: string): Observable<Item[]> {
    return this.http.get<Item[]>(`${environment.apiUrl}/A25/synth/${language}/?v=${this.version}`);
  }

  getSynth(slug: string, language: string): Observable<Item> {
    return this.http.get<Item>(`${environment.apiUrl}/A25/synth/${slug}/${language}/?v=${this.version}`);
  }

  getRecipeList(language: string): Observable<RecipeTab[]> {
    return this.http.get<RecipeTab[]>(`${environment.apiUrl}/A25/recipe/${language}/?v=${this.version}`);
  }

  getCharaList(language: string): Observable<Character[]> {
    return this.http.get<Character[]>(`${environment.apiUrl}/A25/character/${language}/?v=${this.version}`);
  }

  getChara(slug: string, language: string): Observable<Character> {
    return this.http.get<Character>(`${environment.apiUrl}/A25/character/${slug}/${language}/?v=${this.version}`);
  }

  getMemoriaList(language: string): Observable<Memoria[]> {
    return this.http.get<Memoria[]>(`${environment.apiUrl}/A25/memoria/${language}/?v=${this.version}`);
  }

  getMemoria(slug: string, language: string): Observable<Memoria> {
    return this.http.get<Memoria>(`${environment.apiUrl}/A25/memoria/${slug}/${language}/?v=${this.version}`);
  }

  getResearch(language: string): Observable<Research[]> {
    return this.http.get<Research[]>(`${environment.apiUrl}/A25/research/${language}/?v=${this.version}`);
  }

  getUpdate(language: string): Observable<Update> {
    return this.http.get<Update>(`${environment.apiUrl}/A25/update/${language}/?v=${this.version}`);
  }

  getDungeons(language: string): Observable<Dungeon[]> {
    return this.http.get<Dungeon[]>(`${environment.apiUrl}/A25/dungeon/${language}/?v=${this.version}`);
  }

  getScoreBattles(language: string): Observable<ScoreBattle[]> {
    return this.http.get<ScoreBattle[]>(`${environment.apiUrl}/A25/scorebattle/${language}/?v=${this.version}`);
  }

  getTower(slug: string, language: string): Observable<Tower[]> {
    const slugname = {
      "fire":"fire",
      "ice":"ice",
      "bolt":"lightning",
      "air":"wind",
      "slash":"slash",
      "strike":"impact",
      "stab":"pierce",
      "elemental-tower":"elemental-tower"
    }
    return this.http.get<Tower[]>(`${environment.apiUrl}/A25/tower/${slugname[slug]}/${language}/?v=${this.version}`);
  }

  getEmblems(language: string): Observable<Emblem[]> {
    return this.http.get<Emblem[]>(`${environment.apiUrl}/A25/emblem/${language}/?v=${this.version}`);
  }
}
