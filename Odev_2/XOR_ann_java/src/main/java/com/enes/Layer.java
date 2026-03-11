package com.enes;

public class Layer {

    public Noron[] layer;
    public Layer nextLayer;
    public Layer preLayer;


    public Layer(Noron[] norons) {
        this.layer = norons;
        this.nextLayer = null;
        this.preLayer = null;
    }

    public Layer(int[] X){


    }

    public Noron[] getLayer() {
        return layer;
    }

    public void setLayer(Noron[] layer) {
        this.layer = layer;
    }

    public Layer getNextLayer() {
        return nextLayer;
    }

    public void setNextLayer(Layer nextLayer) {
        this.nextLayer = nextLayer;
    }

    public Layer getPreLayer() {
        return preLayer;
    }

    public void setPreLayer(Layer preLayer) {
        this.preLayer = preLayer;
    }


}