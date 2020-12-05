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
            <Link to="/HW4.exe" target="_blank" download>Download Benign File</Link>
            </li>
            <li>
            <Link to="/mal.exe" target="_blank" download>Download Malware File</Link>
            </li>
            <li>
            <a href="/HW4.exe" target="_blank">Download New Window</a>
            </li>
          </ul>
        </nav>
      </div>
    </Router>
  );
}
