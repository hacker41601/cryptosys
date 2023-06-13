#include <bits/stdc++.h> //avoid missing libraries running code
using namespace std;


int main()
{

	int coinkydink = 0; //everyone I knew working on this was using some form of the word coincidence so coinkydink is just another way of saying it

	int max_dinks = 0; //initialize the max number of coincidences

	int bestLength = 0; //this will determine the keylength (which I know is EASY)

	int maxLength = 6; //the parameters in the homework said it could be up to 6 letters long

	int numAppearances = 0; //the number of appearances a letter makes every given key length

	string ciphertext = "xhwdmtfcwsypemhygejrislgwaesptaqxayceejmfiuaepsamtqrislrlalnvoypiskgzedwkelqqojchixdmcmjxakgxcglxifsislfitocrtqkitwptaucvtwqxajpbwemnalxhapxykcgofbwlaliuhyxtzcwtspxtzcvuflmnyqtewbwtspxskjswdwfuleitkdeslcvesalmalytwyjtwpcomfiajrlikqmgfypakgrgdcpahqlomjhbwasmhjitwbiaufxieccomfiajrlikqsufbveecqbwpxojsrifywtjymgzrpifcenvpynsqpofeeshmwsazpelfiswasnvrmmwwsuxymllmgoenpelcelsnfexmvelfisgsrdqmyrlcwtaqsvwpxhwrislumldzigalsnlfiwgphslyvtglcompqajikelpiavwwtspx";

	for (int i = 1; i < maxLength; i++) //outer loop representing the possible number of key lengths
	{
		for (int j = 0; (j+i) < ciphertext.length(); j++) //the second loop iterates through the first and shifts to see how ften the letters will match up and count them
		{
			if (ciphertext[j] == ciphertext[j+i]) //this is if the current iteration matches the original
			{
				coinkydink++; //the number of coincidences will increase
			}
			if (coinkydink > max_dinks) //if the number of coincidenes are greater than the max, the max will reset to match the number of coincidenes
			{
				max_dinks = coinkydink;
				bestLength = i; //the best length is how often it appears
			}

		}
		coinkydink = 0; //reinitialize
	}

	cout << bestLength << endl; //printing the results
/*
	for (int i = 0; i < ciphertext.length(); i+=bestLength)
	{
		if (ciphertext[i] == ciphertext[i+bestLength])
		{
			numAppearances++;
		}
	}

	cout << numAppearances << endl;
*/

	return 0;
}

