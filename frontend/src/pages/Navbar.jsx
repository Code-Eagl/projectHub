import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="navbar">
      <h2>Fake News Detector</h2>
      <div>
        <Link to="/">Home</Link>
        <Link to="/algorithm">Algorithm</Link>
        <Link to="/libraries">Libraries</Link>
      </div>
    </nav>
  );
}
