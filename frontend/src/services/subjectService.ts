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
