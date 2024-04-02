import QtQuick 2.5
import QtQuick.Controls 2.5
import QtMultimedia

ApplicationWindow {
    visible:true
    width:600
    height:400
    title:"Play Videos"

    MediaPlayer {
        id:player
        source:"20_seconds_render.mp4"
        audioOutput:audioOutput
        videoOutput:videoOutput
    }

    AudioOutput {
        id:audioOutput
        volume:volumeSlider.value
    }
    VideoOutput {
        id:videoOutput
        anchors.fill:parent
    }

    Component.onCompleted : {
        player.play()
    }

    Slider {
        id:volumeSlider
        anchors.top:parent.top
        anchors.right:parent.right
        anchors.margin:20
        orientation:Qt.Vertical
        value:0.5
    }
}