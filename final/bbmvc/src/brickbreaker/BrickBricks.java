package brickbreaker;

import java.util.Random;

public class BrickBricks {

    private Random rand = new Random();

    private int hitsToBreak;


    public BrickBricks() {
        this.hitsToBreak = rand.nextInt(3) + 1;
    }

    /** Returns current position of brick.
     *
     * @return A tuple containing the x-coordinate and y-coordinate
     */
    private void getPosition() {

    }

    /** Reduces life of brick by 1 after being hit.
     */
    private void onHit() {
        this.hitsToBreak--;
    }
}