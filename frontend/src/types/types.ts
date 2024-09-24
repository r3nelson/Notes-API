export interface FlashCard {
  id: number;
  question: string;
  answer: string;
  confidence: number;
  subject_id?: number;
  subject_name?: string;
}

export interface Subject {
  id: number;
  name: string;
  continuations?: string[];
}
