export default function Algorithm() {
  return (
    <div className="container">
      <h1>Algorithm Used</h1>

      <p>
        This project uses <strong>DistilBERT</strong>, a lightweight version of
        BERT, for Fake News Detection.
      </p>

      <ol>
        <li>News article is taken as input</li>
        <li>Text is cleaned and tokenized</li>
        <li>Tokens are passed to DistilBERT model</li>
        <li>Model predicts whether news is Fake or Real</li>
        <li>Probabilities are returned as output</li>
      </ol>

      <p>
        DistilBERT provides high accuracy while being faster and computationally
        efficient.
      </p>
    </div>
  );
}
