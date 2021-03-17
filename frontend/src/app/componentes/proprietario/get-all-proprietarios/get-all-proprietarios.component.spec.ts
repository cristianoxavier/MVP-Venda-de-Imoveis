import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GetAllProprietariosComponent } from './get-all-proprietarios.component';

describe('GetAllProprietariosComponent', () => {
  let component: GetAllProprietariosComponent;
  let fixture: ComponentFixture<GetAllProprietariosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GetAllProprietariosComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GetAllProprietariosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
