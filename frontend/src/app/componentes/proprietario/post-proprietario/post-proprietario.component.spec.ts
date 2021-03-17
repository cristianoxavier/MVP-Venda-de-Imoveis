import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PostProprietarioComponent } from './post-proprietario.component';

describe('PostProprietarioComponent', () => {
  let component: PostProprietarioComponent;
  let fixture: ComponentFixture<PostProprietarioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PostProprietarioComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PostProprietarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
