#!/usr/bin/node
function facrtorial(a){
        if (a ===0){
                return (1);
        }
        return a * facrtorial(a - 1);
}
facrtorial(parseInt(process.argv[2]));
