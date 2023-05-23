#include<stdio.h>
#include<stdlib.h>
#include <string.h>

int main(){
    printf("[Initialisation]\n");
    printf("[POD 099 at your service]\n");
    printf("[Please let us write your description :]\n");

    char human_confirmation[4];
    char gender[10];
    int age;
    char day[2], month[2], year[4];
    char hair_color[15];
    char eye_color[15];
    int height;
    int weight;
    char job[20];
    char like[20];
    char dislike[20];
    char strong_point[20];
    char weak_point[20];
    char house[20];
    int n_lan;
    char born[20];
    char relation[20];
    char accomplishment[20];
    char fear[20];
    char future[20];

    char n_choice;
    //1
    while(1){
        printf("[Are you a human ?]\n");
        printf("Y) Yes / N) no -> ");
        scanf("%c", &n_choice);
        //printf("n_choice = %d\n", n_choice);
        if(n_choice == 'Y'){
            strcpy(human_confirmation,"Yes");
            break;
        }
        else if(n_choice == 'N'){
            strcpy(human_confirmation,"no");
            break;
        }
        else{
            printf("Input error, try again\n-> ");
        }
    }
    //printf("test = %s", human_confirmation);
    //2
    printf("\n[What is your Gender ?]\n");
    printf("Male, Female, Non-binary -> ");
    scanf("%s", &gender);
    //3
    printf("\n[How old are you ?]\n");
    printf("Enter a Number : ");
    scanf("%d", &age);
    //4
    printf("\n[What is your birthdate ?]\n");
    printf("Please enter : Day number, month number, year number like 01 02 2000 \n day -> ");
    scanf("%s", &day);
    printf("\nmonth -> ");
    scanf("%s", &month);
    printf("\nyear -> ");
    scanf("%s", &year);
    //5
    printf("\n[What is your hair color ?]\n");
    printf("-> ");
    scanf("%s", &hair_color);
    //6
    printf("\n[What colour are your eyes ?]\n");
    printf("-> ");
    scanf("%s", &eye_color);
    //7
    printf("\n[What is your height ?]\n");
    printf("Enter a Number in cm : ");
    scanf("%d", &height);
    //8
    printf("\n[What is your weight ?]\n");
    printf("Enter a Number in kg : ");
    scanf("%d", &height);
    //9
    printf("\n[What is your profession ?]\n");
    printf("-> ");
    scanf("%s", &job);
    //10
    printf("\n[What do you like ?]\n");
    printf("-> ");
    scanf("%s", &like);
    //11
    printf("\n[What do you hate ?]\n");
    printf("-> ");
    scanf("%s", &dislike);
    //12
    printf("\n[Gime me one of your strong point ?]\n");
    printf("-> ");
    scanf("%s", &strong_point);
    //13
    printf("\n[Gime me one of your weak point ?]\n");
    printf("-> ");
    scanf("%s", &weak_point);
    //14
    printf("\n[Where do you live ?]\n");
    printf("-> ");
    scanf("%s", &house);
    //15
    printf("\n[How many Languages can you speak ?]\n");
    printf("-> ");
    scanf("%d", &n_lan);
    //16
    printf("\n[Where are you born ?]\n");
    printf("-> ");
    scanf("%s", &born);
    //17
    printf("\n[Are you in a relationship ?]\n");
    printf("yes / no -> ");
    scanf("%s", &relation);
    //18
    printf("\n[What is your greatest accomplishment ?]\n");
    printf("-> ");
    scanf("%s", &accomplishment);
    //19
    printf("\n[Do you fear death ?]\n");
    printf("yes / no -> ");
    scanf("%s", &fear);
    //20
    printf("\n[Any plan for your future ?]\n");
    printf("-> ");
    scanf("%s", &future);


    printf("\n\n[Here are your resume :]\n");
    printf("human_confirmation = %s\n",human_confirmation);
    printf("gender = %s\n",gender);
    printf("human_confirmation = %d\n",age);
    printf("Birthdate = %s/%s/%s\n",day, month, year);
    printf("Hair Color = %s\n",hair_color);
    printf("Eye Color = %s\n",eye_color);
    printf("Height = %d cm\n",height);
    printf("Weight = %d kg\n",weight);
    printf("Job = %s\n",job);
    printf("Like = %s\n",like);
    printf("Dislike = %s\n",dislike);
    printf("Strong Point = %s\n",strong_point);
    printf("Weak Point = %s\n",weak_point);
    printf("Living in = %s\n",house);
    printf("Number of Languages learned = %d\n",n_lan);
    printf("Place of Birth = %s\n",born);
    printf("Relationship = %s\n",relation);
    printf("Biggest Accomplisment = %s\n",accomplishment);
    printf("Fear of Death = %s\n",fear);
    printf("Future Plans = %s\n",future);

    return 0;
}