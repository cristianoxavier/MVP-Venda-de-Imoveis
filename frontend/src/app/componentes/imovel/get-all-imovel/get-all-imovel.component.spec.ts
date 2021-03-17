import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GetAllImovelComponent } from './get-all-imovel.component';

describe('GetAllImovelComponent', () => {
  let component: GetAllImovelComponent;
  let fixture: ComponentFixture<GetAllImovelComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GetAllImovelComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GetAllImovelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
