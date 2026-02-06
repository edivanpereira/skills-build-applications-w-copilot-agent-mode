import React, { useEffect, useState } from 'react';

export default function Teams() {
  const [items, setItems] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const baseUrl = codespace ? `https://${codespace}-8000.app.github.dev` : 'http://localhost:8000';
  const endpoint = `${baseUrl}/api/teams/`;

  useEffect(() => {
    console.log('Fetching Teams from', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Teams fetched:', data);
        const list = data && data.results ? data.results : data;
        setItems(Array.isArray(list) ? list : []);
      })
      .catch(err => console.error('Teams fetch error:', err));
  }, [endpoint]);

  return (
    <div>
      <h3>Teams</h3>
      <ul className="list-group">
        {items.map((it, idx) => (
          <li className="list-group-item" key={idx}>{it.name || JSON.stringify(it)}</li>
        ))}
      </ul>
    </div>
  );
}
