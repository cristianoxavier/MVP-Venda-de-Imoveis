import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PostImovelComponent } from './post-imovel.component';

describe('PostImovelComponent', () => {
  let component: PostImovelComponent;
  let fixture: ComponentFixture<PostImovelComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PostImovelComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PostImovelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
