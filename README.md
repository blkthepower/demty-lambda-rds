# demty-lambda-rds

Shows a lambda that connects to a MYSQL instance in RDS

It's important to remember that both the database and the lambda should be in the same VPC and the security groups should allow inbound and outbund connections.

# Loading the lambda

The contents of "site-packages" and the whole "app" folder should be packed in a single ZIP file. After loading the ZIP file into the lambda, the handler must be 
changed to `app.lambda_function.lambda_handler`, just like the file's structure.

## Enviroment varibales

The following lambda environment variables are required to exeute the lambda:

### `DB_HOST`
- **Type**: `string`
- **Description**: Endpoint of the RDS database.
  
### `DB_NAME`
- **Type**: `string`
- **Description**: Database name to be used.

### `DB_TABLE`
- **Type**: `string`
- **Description**: Table name to query.

### `DB_USER`
- **Type**: `string`
- **Description**: Database user.

### `DB_PASS`
- **Type**: `string`
- **Description**: User password.

