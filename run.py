import os
from project import main

if __name__ == '__main__':
    port = 5000
    main.app.run(host='0.0.0.0', port=port)
