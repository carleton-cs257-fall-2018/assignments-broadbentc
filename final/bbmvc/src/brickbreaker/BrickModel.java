package brickbreaker;

import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.AnchorPane;
import javafx.scene.shape.Rectangle;

import java.util.Timer;
import java.util.TimerTask;

public class BrickModel {

    @FXML private Button pauseButton;
    @FXML private Label scoreLabel;
    @FXML private AnchorPane gameBoard;
    @FXML private Rectangle paddle;
    @FXML private BrickBall ball;

    final private double FRAMES_PER_SECOND = 60.0;


    private int score;

    private Timer timer;

    public BrickModel(){
        this.startTimer();
    }

    private void startTimer() {
        this.timer = new java.util.Timer();
        TimerTask timerTask = new TimerTask() {
            public void run() {
                Platform.runLater(new Runnable() {
                    public void run() {
                        updateAnimation();
                    }
                });
            }
        };

        long frameTimeInMilliseconds = (long)(1000.0 / FRAMES_PER_SECOND);
        this.timer.schedule(timerTask, 0, frameTimeInMilliseconds);
    }

    public void movePaddleLeft() {
        double paddlePosition = this.paddle.getLayoutX();
        double stepSize = 5.0;
        if (paddlePosition > stepSize) {
            this.paddle.setLayoutX(this.paddle.getLayoutX() - stepSize);
        } else {
            this.paddle.setLayoutX(0);
        }
    }


    public void movePaddleRight() {
        double paddlePosition = this.paddle.getLayoutX();
        double stepSize = 5.0;
        if (paddlePosition + this.paddle.getWidth() + stepSize < this.gameBoard.getWidth()) {
            this.paddle.setLayoutX(this.paddle.getLayoutX() + stepSize);
        } else {
            this.paddle.setLayoutX(this.gameBoard.getWidth() - this.paddle.getWidth());
        }
    }

    public void pauseGame() {
        this.pauseButton.setText("Pause");
        this.startTimer();
    }

    public void unpauseGame() {
        this.pauseButton.setText("Continue");
        this.timer.cancel();
    }

    private void updateAnimation() {
        double ballCenterX = this.ball.getCenterX() + this.ball.getLayoutX();
        double ballCenterY = this.ball.getCenterY() + this.ball.getLayoutY();
        double ballRadius = this.ball.getRadius();
        double paddleTop = this.paddle.getY() + this.paddle.getLayoutY();
        double paddleLeft = this.paddle.getX() + this.paddle.getLayoutX();
        double paddleRight = paddleLeft + this.paddle.getWidth();

        // Bounce off paddle. NOTE: THIS IS A BAD BOUNCING ALGORITHM. The ball can badly
        // overshoot the paddle and still "bounce" off it. See if you can come up with
        // something better.
        if (ballCenterX >= paddleLeft && ballCenterX < paddleRight && this.ball.getVelocityY() > 0) {
            double ballBottom = ballCenterY + ballRadius;
            if (ballBottom >= paddleTop) {
                this.ball.setVelocityY(-this.ball.getVelocityY());
                this.score++;
                this.scoreLabel.setText(String.format("Bounces: %d", this.score));
            }
        }

        // Bounce off walls
        double ballVelocityX = this.ball.getVelocityX();
        double ballVelocityY = this.ball.getVelocityY();
        if (ballCenterX + ballRadius >= this.gameBoard.getWidth() && ballVelocityX > 0) {
            this.ball.setVelocityX(-ballVelocityX);
        } else if (ballCenterX - ballRadius < 0 && ballVelocityX < 0) {
            this.ball.setVelocityX(-ballVelocityX);
        } else if (ballCenterY + ballRadius >= this.gameBoard.getHeight() && ballVelocityY > 0) {
            this.ball.setVelocityY(-ballVelocityY);
        } else if (ballCenterY - ballRadius < 0 && ballVelocityY < 0) {
            this.ball.setVelocityY(-ballVelocityY);
        }

        // Move the sprite.
        this.ball.step();
    }

}
