import { TestBed } from '@angular/core/testing';

import { ApiImoveisService } from './api-imoveis.service';

describe('ApiImoveisService', () => {
  let service: ApiImoveisService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ApiImoveisService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
