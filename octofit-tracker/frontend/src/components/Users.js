import React, { useEffect, useState } from 'react';

export default function Users() {
  const [items, setItems] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const baseUrl = codespace ? `https://${codespace}-8000.app.github.dev` : 'http://localhost:8000';
  const endpoint = `${baseUrl}/api/users/`;

  useEffect(() => {
    console.log('Fetching Users from', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Users fetched:', data);
        const list = data && data.results ? data.results : data;
        setItems(Array.isArray(list) ? list : []);
      })
      .catch(err => console.error('Users fetch error:', err));
  }, [endpoint]);

  return (
    <div>
      <h3>Users</h3>
      <ul className="list-group">
        {items.map((it, idx) => (
          <li className="list-group-item" key={idx}>{it.email || it.name || JSON.stringify(it)}</li>
        ))}
      </ul>
    </div>
  );
}
