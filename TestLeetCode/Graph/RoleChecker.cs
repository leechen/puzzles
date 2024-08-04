using System;

// Snowflake 2024
// Problem: Our team is building a role based authz model, where a user is authorized if they have specific role assigned to them. Multiple roles can be assigned to a user. A role can inherit other roles. 

// In backend we store the relationship between role in a pair. Ie. [4,2], where role 4 inherits role 2. 

// Build a method to identify if a given role is assigned to user.
// Input to the method - 
//     - Role Relationship =[(4,2),(4,3),(2,0),(2, 1),(3, 1)]
//         ○ In this case [4,2], Role 4 inherits Role 2 
//     - Roles assigned to User: [4]
//     - Role that we need to check : '2'

// Sample output - > 
//     - check for 4 or 0 should return true
// Check for 5 should return false

class RoleRelation {
    public int To;
    public int From;
}

class RoleChecker {
    private IList<RoleRelation> roleRelations;
    private HashSet<int> roles;
    private IDictionary<int, IList<int>> roleAdj;
    private HashSet<int> visited;

    public RoleChecker(IList<RoleRelation> roleRelations) {
        this.roleRelations = roleRelations;
        BuildGraph(roleRelations);
    }

    private void BuildGraph(IList<RoleRelation> roleRelations)
    {
        foreach(var roleRelation in roleRelations) 
        {
            if (!roleAdj.ContainsKey(roleRelation.To)) {
                roleAdj[roleRelation.To] = new List<int>();
            }
            roleAdj[roleRelation.To].Add(roleRelation.From);
        }
    }

    public void Assign(IList<int> roles) {
        this.roles = new HashSet<int>(roles);
    }

    public bool HasRole(int role) {
        visited = new HashSet<int>();
        return Helper(role);
    }

    private bool Helper(int role) {
        if (visited.Contains(role)) { return false; }
        visited.Add(role);
        if (roles.Contains(role)) { return true; }

        foreach(var derivedRole in roleAdj[role]) {
            if (Helper(derivedRole)) { return true; }
        }

        return false;
    }
}
// Your previous Plain Text content is preserved below:

// This is just a simple shared plaintext pad, with no execution capabilities.

// When you know what language you'd like to use for your interview,
// simply choose it from the dots menu on the tab, or add a new language
// tab using the Languages button on the left.

// You can also change the default language your pads are created with
// in your account settings: https://app.coderpad.io/settings

// Enjoy your interview!