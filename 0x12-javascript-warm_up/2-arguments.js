#!/usr/bin/node
import { argv } from 'node:process';

// print process.argv
if (argv.length > 1) {
        console.log("No argument");
} else {
        console.log("Argument found");
}
