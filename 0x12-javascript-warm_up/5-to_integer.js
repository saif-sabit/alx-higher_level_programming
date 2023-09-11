import { argv } from 'node:process';
if (parseInt(argv[1]) ==NaN){
        console.log("Not a number")
}else{
        console.log("My number:"+parseInt(argv[1]))
}
