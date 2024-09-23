// Displays a single subject
import { Subject } from "../../types/types";

const SubjectItem: React.FC<{ subject: Subject }> = ({ subject }) => {
  return (
    <div
      style={{
        border: "1px solid #ccc",
        padding: "10px",
        marginBottom: "10px",
      }}
    >
      <p>
        <strong>Name:</strong> {subject.name}
      </p>
      <p>
        <strong>Continuations:</strong> {subject.continuations}
      </p>
    </div>
  );
};

export default SubjectItem;
