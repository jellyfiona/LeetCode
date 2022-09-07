
int LtoInt(char c){
    
    switch (c){
        case 'I' : return 1;
        case 'V' : return 5;
        case 'X' : return 10;
        case 'L' : return 50;
        case 'C' : return 100;
        case 'D' : return 500;
        case 'M' : return 1000;
        default: return 0;
    }
    
    
}

/*
[approach] we iterate the string char one by one and add the value of each char to the sum.
If we see a char whose value is smaller than the last char's value, we substact the sum by last value times 2.
That is how we make it right.
time_O(N) we iterate the string once.
spact_O(1) we only need to store last char's value.

*/
int romanToInt(char * s){
    char * p = NULL;
    int curInt = 0;
    int lastInt = 0;
        
    int output = 0;
    if (s == NULL){
        return 0;
    }
    
    p = s;
    for ( p = s; *p!= '\0'; p++){
        curInt = LtoInt(*p);
        output = output + curInt;
        if (lastInt != 0 && lastInt < curInt){
            output = output - 2* lastInt;
        }         
        lastInt = curInt;  
    }
    return output;
}