Key Technical Features:

 - **Decoupling Logic**: Each country's fee calculation is encapsulated in its own strategy class.

 - **Factory Pattern**: Dynamically instantiates the correct strategy based on user input.

 - **Extensibility**: Adding a new logistics strategy requires 0 modification to existing code.
  
Structure:

- `logistics.py`: Core logic