import { useMemo } from 'react';

function ActiveUsersList({ users }) {
  const visibleUsers = useMemo(() => {
    return users.filter((user) => user.isActive);
  }, [users]);

  return (
    <div>
      <ul>
        {visibleUsers.map((user) => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </div>
  );
}