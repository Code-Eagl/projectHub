import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Algorithm from "./pages/Algorithm";
import Libraries from "./pages/Libraries";
import Navbar from "./pages/Navbar";

export default function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/algorithm" element={<Algorithm />} />
        <Route path="/libraries" element={<Libraries />} />
      </Routes>
    </BrowserRouter>
  );
}
