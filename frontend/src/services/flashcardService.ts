// API functions for flashcards (GET, POST, PATCH, DELETE)
import { FlashCard } from "../types/types";

const API_URL = import.meta.env.VITE_API_URL; // ask about this line

// Fetch all Flashcards
export const fetchFlashcards = async (): Promise<FlashCard[]> => {
  console.log(`API_URL: ${API_URL}`);
  const response = await fetch(`${API_URL}/flashcards`);
  //   const response = await fetch(`http://localhost:8000/api/flashcards`);

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
