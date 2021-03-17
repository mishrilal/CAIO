import QtQuick 2.15
import QtQuick.Controls 2.15
import "../controls"


Item {
    id: item1
    Rectangle {
        id: rectangle
        color: "#2c313c"
        anchors.fill: parent

        Label {
            id: textAddFace
            color: "#ffffff"
            text: qsTr("Add a Face")
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 10
            font.pointSize: 16
        }

        Rectangle {
            id: cameraArea
            color: "#00000000"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: textAddFace.bottom
            anchors.bottom: captureBtnArea.top
            anchors.bottomMargin: 100
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 49

            Rectangle {
                id: rectangle1
                x: 357
                width: cameraArea.height
                color: "#00000000"
                radius: 10
                border.width: 3
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.bottomMargin: 0
                anchors.topMargin: 0

                Label {
                    id: cameraLabel
                    color: "#ffffff"
                    text: qsTr("Camera is OFF or Not Working")
                    anchors.fill: parent
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                }
            }



//            CameraFeed {
//                x: 329
//                width: cameraArea.height
//                anchors.top: parent.top
//                anchors.bottom: parent.bottom
//                anchors.horizontalCenter: parent.horizontalCenter
//                anchors.bottomMargin: 0
//                anchors.topMargin: 0
//            }

        }

        Connections {
            target: addFaceBackend
            function onSetCameraLabel(value) {
                cameraLabel.setPixmap(value)
            }

        }

        Rectangle {
            id: captureBtnArea
            y: 333
            height: 60
            color: "#00000000"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.bottomMargin: 40

            CaptureBtn {
                anchors.horizontalCenter: parent.horizontalCenter
            }
        }

        //        Connections{
        //            target: backend
        //        }


    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:473;width:908}
}
##^##*/
