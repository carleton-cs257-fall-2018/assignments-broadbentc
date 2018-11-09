package brickbreaker;

public class GameInfo {

    private int lives;
    private int level;
    private int bricksLeft;

    public GameInfo() {
        this.lives = 3;
        this.level = 1;
        this.bricksLeft = 15;
    }


    /** Reduces lives by 1 when ball goes past paddle.
     *
     */
    private void lifeLost() {
        this.lives--;
    }

    /** Returns current number of lives.
     *
     * @return integer value of lives
     */
    private int getLives() {
        return this.lives;
    }

    /** Reduces brick count by 1 when brick is destroyed.
     *
     */
    private void brickDestroyed() {
        this.bricksLeft--;
    }

    /** Returns current number of bricks left.
     *
     * @return integer value of number of bricks left.
     */
    private int getBricksLeft() {
        return this.bricksLeft;
    }

    /** Checks if there are no bricks left. If so, go to next level.
     *
     */
    private void bricksLeftCheck() {
        if (this.bricksLeft==0) {
            this.level++;
        }

    }

    /** Returns current level.
     *
     * @return integer of current level
     */
    private int getLevel() {
        return this.level;
    }
}