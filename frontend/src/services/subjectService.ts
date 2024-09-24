// API functions for subjects (GET, POST, PATCH, DELETE)
import { Subject } from "../types/types";

const API_URL = import.meta.env.VITE_API_URL;

// Fetch Subjects
export const fetchSubjects = async (): Promise<Subject[]> => {
  const response = await fetch(`${API_URL}/subjects`);
  if (!response.ok) {
    throw new Error(`Error fetching subjects: ${response.statusText}`);
  }
  const data: Subject[] = await response.json();
  return data;
};

// Create a Subject
export const createSubject = async (
  subject: Omit<Subject, "id">
): Promise<void> => {
  const response = await fetch(`${API_URL}/subjects`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(subject),
  });

  if (!response.ok) {
    const errorDetails = await response.json(); // Try to parse the error details
    throw new Error(
      `Error fetching subjects: ${response.statusText}. Details: ${errorDetails.detail}`
    );
  }
};
