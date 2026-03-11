package com.enes;

public class AktivasyonFunc {


    public double sigmodiFunc(float h){
        double sonuc = 1 / (1+ Math.exp(-h));
        return sonuc;
    }

    public double deSigmoidFunc(float h){
        return Math.exp(-h)/( (1+Math.exp(h)) * (1+Math.exp(h)) );
    }

}
