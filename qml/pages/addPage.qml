import QtQuick 2.15
import QtQuick.Controls 2.15
import "../controls"


Item {
    Rectangle {
        id: rectangle
        color: "#2c313c"
        anchors.fill: parent

        Label {
            id: label
            color: "#ffffff"
            text: qsTr("Add a Face")
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 3
            font.pointSize: 16
        }

        Rectangle {
            id: rectangle1
            height: 200
            color: "#00000000"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: label.bottom
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 49

            CameraFeed {
                x: 329
                width: 250
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 0
                anchors.topMargin: 0
                anchors.horizontalCenter: parent.horizontalCenter

            }
        }


    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:473;width:908}D{i:2}D{i:4}D{i:3}
}
##^##*/
