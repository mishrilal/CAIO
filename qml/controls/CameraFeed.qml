import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    id: cameraArea
    color: "#00000000"
    radius: 10
    border.width: 3
    width: 200
    height: 200
    Label {
        id: cameraFeed
        color: "#ffffff"
        text: qsTr("Camera Not Working")
        anchors.fill: parent
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        clip: true
    }

}

/*##^##
Designer {
    D{i:0;height:250;width:250}
}
##^##*/
