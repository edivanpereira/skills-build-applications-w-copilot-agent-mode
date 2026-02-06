import React, { useEffect, useState } from 'react';

export default function Leaderboard() {
  const [items, setItems] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const baseUrl = codespace ? `https://${codespace}-8000.app.github.dev` : 'http://localhost:8000';
  const endpoint = `${baseUrl}/api/leaderboard/`;

  useEffect(() => {
    console.log('Fetching Leaderboard from', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Leaderboard fetched:', data);
        const list = data && data.results ? data.results : data;
        setItems(Array.isArray(list) ? list : []);
      })
      .catch(err => console.error('Leaderboard fetch error:', err));
  }, [endpoint]);

  return (
    <div>
      <h3>Leaderboard</h3>
      <ol className="list-group list-group-numbered">
        {items.map((it, idx) => (
          <li className="list-group-item" key={idx}>{it.user || it.name || JSON.stringify(it)}</li>
        ))}
      </ol>
    </div>
  );
}
