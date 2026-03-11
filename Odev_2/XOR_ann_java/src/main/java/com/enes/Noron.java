package com.enes;

import java.util.List;
import java.util.Random;

public class Noron {

    public int[] girdi;
    public float[] agirliklar;

    Random random = new Random();


    Noron(int[] X){

        this.girdi=X;
    }

    public float sumFunc(int[] xList , float[] wList,float bias) {
        float sum = 0f;

        for (int i = 0; i <= (xList.length - 1); i++) {
            sum = sum + xList[i] * wList[i];
        }

        sum = sum + bias;
        return sum;
    }

}
