// Form to create or edit subjects
import { Subject } from "../../types/types";
import { createSubject } from "../../services/subjectService";
import React, { useState } from "react";

const SubjectForm: React.FC = () => {
  const [name, setName] = useState<string>("");
  const [continuations, setContinuations] = useState<string[]>([]);
  const [continuationsInput, setContinuationsInput] = useState<string>("");
  const [error, setError] = useState<string | null>("");
  const [successMessage, setSuccessMessage] = useState<string | null>(null);

  const handleAddContinuations = () => {
    const newContinuations = continuationsInput
      .split(",")
      .map((item) => item.trim())
      .filter((item) => item); // Split and trim
    setContinuations((cur) => [...cur, ...newContinuations]); // Update the continuations array
    setContinuationsInput(""); // Clear the input after adding
  };

  const handleSubjectSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    const subject: Omit<Subject, "id"> = {
      name,
      continuations,
    };

    try {
      console.log(`subject: ${subject}`);
      await createSubject(subject);
      setName("");
      setContinuationsInput("");
      setContinuations([]);
      setError(null);
      setSuccessMessage("Subject created successfully!");
    } catch (err) {
      setError(`Failed to create subject.\nError: ${err}`);
      console.log(error);
    }
  };

  return (
    <div>
      <h2>Create a New Subject</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {successMessage && <p style={{ color: "green" }}>{successMessage}</p>}

      <form onSubmit={handleSubjectSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>

        <div>
          <label htmlFor="continuations">Continuations:</label>
          <input
            type="text"
            id="continuations"
            value={continuationsInput}
            onChange={(e) => setContinuationsInput(e.target.value)}
          />
          <button type="button" onClick={handleAddContinuations}>
            +
          </button>
          <h3>Current Continuations:</h3>
          <ul>
            {continuations.map((continuation, index) => (
              <li key={index}>{continuation}</li>
            ))}
          </ul>
        </div>

        <button type="submit">Create Flashcard</button>
      </form>
    </div>
  );
};

export default SubjectForm;
