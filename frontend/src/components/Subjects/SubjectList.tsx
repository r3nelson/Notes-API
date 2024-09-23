// Displays a list of subjects
import SubjectItem from "./SubjectItem";
import useSubjects from "../../hooks/useSubjects";

const SubjectsDisplay: React.FC = () => {
  const { subjects, error } = useSubjects();

  return (
    <div>
      <h1>Subjects</h1>
      {error && <p>{error}</p>}
      {subjects.length > 0 ? (
        <ul>
          {subjects.map((subject) => (
            <li key={subject.id}>
              <SubjectItem subject={subject} />
            </li>
          ))}
        </ul>
      ) : (
        <p> No subjects available</p>
      )}
    </div>
  );
};

export default SubjectsDisplay;
