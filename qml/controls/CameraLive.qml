import QtQuick 2.0
import QtMultimedia 5.15
Rectangle {
    id: cameraRectangle
    color: "#00000000"

    Camera {
        id: camera

    }

    VideoOutput {
        anchors.verticalCenter: parent.verticalCenter
        anchors.top: parent.top
        source: camera
        clip: false
        anchors.horizontalCenter: parent.horizontalCenter
        focus : visible // to receive focus and capture key events when visible
    }


}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
