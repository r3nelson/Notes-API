// Form to create or edit flashcards
import { FlashCard } from "../../types/types";
import { createFlashcard } from "../../services/flashcardService";
import React, { useState } from "react";

const FlashcardForm: React.FC = () => {
  const [question, setQuestion] = useState<string>("");
  const [answer, setAnswer] = useState<string>("");
  const [confidence, setConfidence] = useState<number>(1.0);
  const [subject_name, setSubjectName] = useState<string>("");
  const [error, setError] = useState<string | null>("");
  const [successMessage, setSuccessMessage] = useState<string | null>(null);

  const handleFlashcardSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    // Validate that subject_name is provided
    if (!subject_name) {
      setError("Please provide Subject Name");
      return;
    }

    const flashcard: Omit<FlashCard, "id"> = {
      question,
      answer,
      confidence,
      subject_name,
    };

    try {
      await createFlashcard(flashcard);
      // Clear the form after successful submission
      setQuestion("");
      setAnswer("");
      setConfidence(0);
      setSubjectName("");
      setSuccessMessage("Flashcard created successfully!");
      setError(null);
    } catch (err) {
      setError(`Failed to create flashcard.\nError: ${err}`);
      console.log(error);
    }
  };

  return (
    <div>
      <h2>Create a New Flashcard</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {successMessage && <p style={{ color: "green" }}>{successMessage}</p>}

      <form onSubmit={handleFlashcardSubmit}>
        <div>
          <label htmlFor="question">Question:</label>
          <input
            type="text"
            id="question"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            required
          />
        </div>

        <div>
          <label htmlFor="answer">Answer:</label>
          <input
            type="text"
            id="answer"
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
            required
          />
        </div>

        <div>
          <label htmlFor="confidence">Confidence:</label>
          <input
            type="number"
            id="confidence"
            value={confidence}
            onChange={(e) => setConfidence(parseFloat(e.target.value))}
            min="1.0"
            max="10.0"
            step="0.5"
            required
          />
        </div>

        <div>
          <label htmlFor="subject_name">Subject Name:</label>
          <input
            type="text"
            id="subject_name"
            value={subject_name}
            onChange={(e) => setSubjectName(e.target.value)}
          />
        </div>

        <button type="submit">Create Flashcard</button>
      </form>
    </div>
  );
};

export default FlashcardForm;
