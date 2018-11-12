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

public class Controller implements EventHandler<KeyEvent> {


    private BrickModel brickModel;

    //private boolean paused;

    public Controller() {
    }

    public void initialize() {
        this.brickModel = new BrickModel();
    }

    private void update() {

    }

    @Override
    public void handle(KeyEvent keyEvent) {
        KeyCode code = keyEvent.getCode();

        if (code == KeyCode.LEFT || code == KeyCode.A) {
            // move paddle left
            this.brickModel.movePaddleLeft();

            keyEvent.consume();
        } else if (code == KeyCode.RIGHT || code == KeyCode.D) {
            // move paddle right
            this.brickModel.movePaddleRight();
            keyEvent.consume();
        }
    }

//    public void onPauseButton(ActionEvent actionEvent) {
//        if (this.paused) {
//            this.brickModel.pauseGame();
//        }
//        else {
//            this.brickModel.unpauseGame();
//        }
//        this.paused = !this.paused;
//    }
}