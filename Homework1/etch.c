#include <stdio.h>
#include <stdlib.h>


int rowSize = 8; //size of the rows
int colSize = 8; //size of the columns

void main(void){

	char input = 'z'; //input from keyboard
	int rows, cols; //for loops
	char panel[8][8]; //size of the panel
	int current_row = 4; //inital y-location
	int current_col = 4; //initial x-location

	printf("New game started:\n\n");
	// Creating array for new game
	for(rows=0;rows<rowSize;rows++){
		for(cols=0;cols<colSize;cols++){
			panel[rows][cols] = ' '; //use o for testing
		}
	}

	while(input!='q'){ //sketch loop

		//Updates sketch
		system("clear");
		for(rows=0;rows<rowSize;rows++){
			for(cols=0;cols<colSize;cols++){
				printf("%c ", panel[rows][cols]);
			}
			printf("\n");
		}
		//scanf("%c", &input); //keyboard input
		//printf("%d",rows);//debugging
		input = getchar();

		switch(input){
			case 'q':
				input = 'q';
				printf("Quitting game...\n");
				break;
			case 'w':
				//sketches up
				if(current_row==4 && current_col==4){
					//printf("Gets in the first if");
					panel[current_row][current_col] = 'x';
					current_row--;
				}else{
					if(current_row<=0){
						current_row = 0;
						panel[current_row][current_col] = 'x';
					}else{
						//printf("%d", current_row); //debugging
						//current_row--;
						//printf("%d", current_row); //debugging
						panel[current_row][current_col] = 'x';
						current_row--;
					}
				}
				break;
			case 'a':
				//sketches left
				if(current_row==4 && current_col==4){
					panel[current_row][current_col] = 'x';
					current_col--;
				}else{
					if(current_col<=0){
						current_col = 0;
						panel[current_row][current_col] = 'x';
					}else{
						current_col--;
						panel[current_row][current_col] = 'x';
					}
				}
				break;
			case 's':
				//sketches down
				if(current_row==4 && current_col==4){
					panel[current_row][current_col] = 'x';
					current_row++;
				}else{
					if(current_row>=7){
						current_row = 7;
						panel[current_row][current_col] = 'x';
					}else{
						current_row++;
						panel[current_row][current_col] = 'x';
					}
				}
				break;
			case 'd':
				//sketches right
				if(current_row==4 && current_col==4){
					panel[current_row][current_col] = 'x';
					current_col++;
				}else{
					if(current_col>=7){
						current_col = 7;
						panel[current_row][current_col] = 'x';
					}else{
						current_col++;
						panel[current_row][current_col] = 'x';
					}
				}
				break;
			case 'c':
				//clears the sketch
				for(rows=0;rows<rowSize;rows++){
					for(cols=0;cols<colSize;cols++){
						panel[rows][cols] = ' ';
					}
				}
				break;
			default:
				//probably does nothing
				break;
		}
	}
}
