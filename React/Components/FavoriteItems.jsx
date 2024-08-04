import { useState } from 'react';

function App() {
  const [items, setItems] = useState([
    { id: 1, name: 'Item 1', description: 'Description 1' },
    { id: 2, name: 'Item 2', description: 'Description 2' },
    // ...
  ]);

  const [favorites, setFavorites] = useState([]);

  const handleFavorite = (itemId) => {
    const item = items.find((item) => item.id === itemId);
    if (item) {
      setFavorites((prevFavorites) => [...prevFavorites, item]);
    }
  };

  return (
    <div>
      <h1>Items</h1>
      <ul>
        {items.map((item) => (
          <li key={item.id}>
            {item.name} - {item.description}
            <button onClick={() => handleFavorite(item.id)}>Favorite</button>
          </li>
        ))}
      </ul>

      <h1>Favorites</h1>
      <ul>
        {favorites.map((item) => (
          <li key={item.id}>{item.name} - {item.description}</li>
        ))}
      </ul>
    </div>
  );
}