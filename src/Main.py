from lib.CafeSystem import System

if __name__ == '__main__':
    SYSTEM = System()
    SYSTEM.initializeSystem()

    
    """
    Test
    
    sample = [
            {
                'id': 1,
                'test': {
                    'name': 'bob'
                }
            },
            {
                'id': 1,
                'test': {
                    'name': 'max'
                }
            }
        ]
        target = 'max'
        for i in range(len(sample)):
            print(sample[i]['test']['name'])
            if sample[i]['test']['name'].lower() == target:
                print("Found target")
            else:
                print("Not target")
    
    """