{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bc2d487f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def showNumbers(limit): \n",
    "    for i in range(0,limit+1): \n",
    "        print(i,end=\" \")\n",
    "    if(i%2==0):\n",
    "            print(\"EVEN\") \n",
    "    else: \n",
    "            print(\"ODD\") \n",
    "\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "12d7988a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2cc0068c",
   "metadata": {},
   "outputs": [],
   "source": [
    "sum=[]\n",
    "def sumofmul(limit):\n",
    "    for number in range(1, limit):\n",
    "        if number%3 == 0:\n",
    "            sum.append(number)\n",
    "        if number%5 == 0:\n",
    "            sum.append(number)\n",
    "        print(sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3d703849",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n",
      "[]\n",
      "[3]\n",
      "[3]\n",
      "[3, 5]\n",
      "[3, 5, 6]\n",
      "[3, 5, 6]\n",
      "[3, 5, 6]\n",
      "[3, 5, 6, 9]\n",
      "[3, 5, 6, 9, 10]\n",
      "[3, 5, 6, 9, 10]\n",
      "[3, 5, 6, 9, 10, 12]\n"
     ]
    }
   ],
   "source": [
    "sumofmul(13)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a2fc5163",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "* \r\n",
      "* * \r\n",
      "* * * \r\n",
      "* * * * \r\n",
      "* * * * * \r\n",
      "* * * * * * \r\n",
      "* * * * * * * \r\n",
      "* * * * * * * * \r\n",
      "* * * * * * * * * \r\n",
      "* * * * * * * * * * \r\n"
     ]
    }
   ],
   "source": [
    "def partern(n):\n",
    "    for i in range(0, n):\n",
    "        for j in range(0, i+1):\n",
    "            print(\"* \",end=\"\")\n",
    "        print(\"\\r\")\n",
    "\n",
    "        \n",
    "        \n",
    "partern(10)     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "121e4e46",
   "metadata": {},
   "outputs": [],
   "source": [
    "def primenumb(n):  \n",
    "    for num in range(0, n):\n",
    "        for i in range(2, num):\n",
    "            if num % i == 0:\n",
    "                break\n",
    "            else:\n",
    "                print(num)\n",
    "                break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1204eb6d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "5\n",
      "7\n",
      "9\n",
      "11\n",
      "13\n",
      "15\n",
      "17\n",
      "19\n",
      "21\n",
      "23\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print(primenumb(25))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "afb70fcf",
   "metadata": {},
   "outputs": [],
   "source": [
    "#5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "fcc7960c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#6\n",
    "def primenum(input_number):\n",
    "\n",
    "  flag = 0\n",
    "\n",
    "  for i in range(2, input_number):\n",
    "    if input_number % i == 0:\n",
    "        flag = 1\n",
    "        break\n",
    "    if flag == 1:\n",
    "        return False\n",
    "    else:\n",
    "        return True\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "15b10350",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "primenum(13)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f445c40",
   "metadata": {},
   "outputs": [],
   "source": [
    "7#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.\n",
    "\n",
    "def fibonacci():\n",
    "    num = int(input(\"Please enter how many numbers would you like in your Fibonacci sequence: \"))\n",
    "    i = 1\n",
    "    if num == 0:\n",
    "        fib = []\n",
    "    elif num == 1:\n",
    "        fib = [1]\n",
    "    elif num == 2:\n",
    "        fib = [1,1]\n",
    "    elif num > 2:\n",
    "        fib = [1,1]\n",
    "        while i < (num - 1):\n",
    "            fib.append(fib[i] + fib[i-1])\n",
    "            i += 1\n",
    "    return fib\n",
    "print (fibonacci())\n",
    "input()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f5be5e94",
   "metadata": {},
   "outputs": [],
   "source": [
    "8#Write a function that ask the user for a string and print out whether this string is a palindrome \n",
    "\n",
    "\n",
    "def checkpal(n):\n",
    "    if n == n(::-1)\n",
    "       print(\"The string is a palindrome.\")\n",
    "    else:\n",
    "        print(\"The string is not a palindrome.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ea047c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "n = 'madam'\n",
    "checkpal(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c080224",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "759569d5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
