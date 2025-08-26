Padlock System 

Qifel means Lock in Arabic :)

--------------------------------------------------------------------------------------

Core System Design

Each time a service has to process personal data, makes a query to Qifel
Each service that calls Qifel has its own set of keys
Qifel internally stores a set of root keys for every user, these root keys are never exposed to calling services
When services call Qifel, they include a secret service key, which is unique to that service
A key derivation algorithm takes a root key and the service key and returns a derived key. The services use the derived keys for encryption and decryption
--------------------------------------------------------------------------------------
Data Categories & Lifecycle Management

For data lifecycle, there are data categories - each user has a different key for every category, hence each category is managed independent of others
For example: a user opting out of something, we can easily block access to the user's personal data related to advertisement by removing the appropriate key
--------------------------------------------------------------------------------------

Traffic Characteristics

Traffic is read-dominated, less than 0.1% of requests are inserts or updates
Multi-gets are implemented as independent get operations in the service
--------------------------------------------------------------------------------------

Why Encryption Over Alternatives
Rejected Approach 1: Deletion Endpoints

Would require each service to implement delete endpoint
Too complex for many microservices
Doesn't work for immutable datasets

Rejected Approach 2: Tokenization

Store personal data in central database, other systems store tokens
Couldn't scale to diverse performance requirements