import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GetClienteComponent } from './get-cliente.component';

describe('GetClienteComponent', () => {
  let component: GetClienteComponent;
  let fixture: ComponentFixture<GetClienteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GetClienteComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GetClienteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
