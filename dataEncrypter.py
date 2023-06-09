{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOwHLOiCJUy0zBpaRfyLyho",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ayushibongirwar/Data-Encrypter/blob/main/dataEncrypter.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DVHCq-2Hthu_",
        "outputId": "1a377e76-4dfd-42b1-f576-786c698d9233"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Actual message: hello cat\n",
            "Encrypted message:  ifmmp dbu\n"
          ]
        }
      ],
      "source": [
        "import re\n",
        "def encrypt_message(message):\n",
        "  encrypted_message=''\n",
        "  for char in message:\n",
        "    if char in message:\n",
        "      if char.isalpha():\n",
        "        shifted_char=chr(ord(char)+1)\n",
        "        if char.isupper():\n",
        "          if shifted_char>'Z':\n",
        "            shifted_char='A'\n",
        "        elif char.islower():\n",
        "          if shifted_char>'z':\n",
        "            shifted_char='a'\n",
        "        encrypted_message+=shifted_char\n",
        "      elif char.isdigit():\n",
        "        encrypted_message+=str(int(char)+1)\n",
        "      else:\n",
        "        encrypted_message+=char\n",
        "  return encrypted_message\n",
        "message=input(\"Actual message: \")\n",
        "print(\"Encrypted message: \",encrypt_message(message))"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "CEl5srBEvCqW"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}