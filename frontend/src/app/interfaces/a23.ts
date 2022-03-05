export interface NameLink {
    slug: string;
    name: string;
}

export interface NameOnly {
    ing: string;
}

export interface Trait {
    slug: string;
    grade: number;
    trans_atk: boolean;
    trans_heal: boolean;
    trans_dbf: boolean;
    trans_buff: boolean;
    trans_wpn: boolean;
    trans_arm: boolean;
    trans_acc: boolean;
    trans_tal: boolean;
    trans_exp: boolean;
    trans_syn: boolean;
    name: string;
    desc: string;
    item_set: NameLink[];
    combo1: NameLink;
    combo2: NameLink;
}

export interface AdvData {
    baseAtt: string;
    attTag0: string;
    actTag0: string;
    min_1_0: string;
    max_1_0: string;
    min_2_0: string;
    max_2_0: string;
}

export interface EffectDataSimple {
    effectlines_set: NameLink[]
}

export interface Effect {
    slug: string;
    name: string;
    desc: string;
    advanced: AdvData[];
    effectdata_set:EffectDataSimple[];
}

export interface GatherItem {
    rank: number;
    priority: number;
    slug: string;
    name: string;
}

export interface GatherNode {
    kind: string;
    tool: string;
    items: GatherItem[];
}

export interface Climate {
    weather: string;
    monsters: NameLink[];
    nodes: GatherNode[];
}

export interface Chest {
    item: NameLink;
    book: NameLink;
}

export interface Area {
    slug: string;
    name: string;
    climate: Climate[];
    chests: Chest[];
}

export interface Region {
    slug: string;
    name: string;
    areas: Area[];
}

export interface Monster {
    slug: string;
    kind: string;
    name: string;
    index: number;
    char1: string;
    char2: string;
    char3: string;
    char4: string;
    ailment0: number;
    ailment1: number;
    ailment2: number;
    ailment3: number;
    ailment4: number;
    ailment5: number;
    ailment6: number;
    ailment7: number;
    ailment8: number;
    ailment9: number;
    ailment10: number;
    resist_mag: string;
    resist_fire: string;
    resist_ice: string;
    resist_thun: string;
    resist_wind: string;
    resist_phys: string;
    desc1: string;
    desc2: string;
    desc3: string;
    desc4: string;
    hp_rank: number;
    str_rank: number;
    def_rank: number;
    spd_rank: number;
    drops: NameLink[];
    location: NameLink[];
}

export interface Category {
    slug: string;
    name: string;
    icon: string;
    items: NameLink[];
}

export interface Book {
    slug: string;
    name: string;
    shop: string;
    note: string;
    items: NameLink[];
}

export interface Equip {
    hp: number;
    mp: number;
    atk: number;
    dfn: number;
    spd: number;
}

export interface CharSlug {
    slug: string;
}

export interface Item {
    slug: string;
    name: string;
    kind: string;
    level: number;
    categories: Category[];
    locations: NameLink[];
    desc1: string;
    desc2: string;
    desc3: string;
    desc4: string;
    char1: string;
    char2: string;
    char3: string;
    char4: string;
    equip: Equip;
    book: NameLink[];
    chars: CharSlug[];
    monsters: NameLink[];
}