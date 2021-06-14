export interface Language {
  id: number;
  name: string;
}

export class Portfolio {
  constructor(public name: string | undefined,
              public surname: string | undefined,
              public age: number | undefined,
              public phoneNumber: string | undefined,
              public githubLink: string | undefined,
              public graph: any)
  { }
}

export class GithubData{
  response: any;

  constructor() {}
}
