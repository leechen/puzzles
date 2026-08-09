from dataclasses import dataclass


@dataclass(frozen=True)
class RoleRelation:
    inheriting: int
    inherited: int


class RoleChecker:
    def __init__(self, relations: list[RoleRelation]):
        self.graph = {}
        for relation in relations: self.graph.setdefault(relation.inheriting, []).append(relation.inherited)
        self.roles = set()

    def assign(self, roles: list[int]) -> None: self.roles = set(roles)

    def has_role(self, role: int) -> bool:
        pending, seen = list(self.roles), set()
        while pending:
            current = pending.pop()
            if current == role: return True
            if current not in seen: seen.add(current); pending.extend(self.graph.get(current, []))
        return False
