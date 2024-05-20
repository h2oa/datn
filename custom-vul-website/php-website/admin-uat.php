<?php include 'header.php'; ?>

<main>
    <h2>Admin Page</h2>
    <p>This is the admin (UAT) page.</p>
    
    <!-- Displaying a list of users -->
    <h3>User List</h3>
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Role</th>
            </tr>
        </thead>
        <tbody>
            <?php
            // Mock data (replace this with actual data if available)
            $users = array(
                array("id" => 1, "name" => "John Doe", "email" => "john@example.com", "role" => "Admin"),
                array("id" => 2, "name" => "Jane Smith", "email" => "jane@example.com", "role" => "User"),
                array("id" => 3, "name" => "Bob Johnson", "email" => "bob@example.com", "role" => "User"),
                // Add more users as needed
            );
            
            // Display user data
            foreach ($users as $user) {
                echo "<tr>";
                echo "<td>{$user['id']}</td>";
                echo "<td>{$user['name']}</td>";
                echo "<td>{$user['email']}</td>";
                echo "<td>{$user['role']}</td>";
                echo "</tr>";
            }
            ?>
        </tbody>
    </table>
</main>

<?php include 'footer.php'; ?>
