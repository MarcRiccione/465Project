import {
  BrowserRouter as Router,
  Link
} from "react-router-dom";

export default function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
            <Link to="/test.txt" target="_blank" download>Download</Link>
            </li>
          </ul>
        </nav>
      </div>
    </Router>
  );
}
