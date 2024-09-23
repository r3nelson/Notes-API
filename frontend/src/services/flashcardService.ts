// API functions for flashcards (GET, POST, PATCH, DELETE)
import { FlashCard } from "../types/types";

const API_URL = import.meta.env.VITE_API_URL; // ask about this line

// Fetch all Flashcards
export const fetchFlashcards = async (): Promise<FlashCard[]> => {
  const response = await fetch(`${API_URL}/flashcards`);

  if (!response.ok) {
    throw new Error(`Error fetching flashcards: ${response.statusText}`);
  }

  const data: FlashCard[] = await response.json();
  return data;
};

// // Fetch a Flashcard
// export const fetchFlashcard = async (
//   flashcard_id: number
// ): Promise<FlashCard> => {
//   const response = await fetch(`${API_URL}/flashcard/${flashcard_id}`);

//   if (!response.ok) {
//     throw new Error(`Error fetching flashcards: ${response.statusText}`);
//   }

//   const data: FlashCard = await response.json();
//   return data;
// };
