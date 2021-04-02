import QtQuick 2.15
import QtQuick.Controls 2.15


Item {
    Rectangle {
        id: rectangle
        color: "#16181d"
        anchors.fill: parent

        Label {
            id: label
            color: "#ffffff"
            text: qsTr("DashBoard Page")
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

        Button {
            id: btnDetectFace
            x: 277
            y: 220
            text: qsTr("Run Detect Face")
            anchors.verticalCenter: parent.verticalCenter
            display: AbstractButton.TextBesideIcon
            anchors.horizontalCenter: parent.horizontalCenter

            onClicked: {
                dashboardBackend.detectFaceClicked()
            }
        }
    }

    Connections {
        target: dashboardBackend
    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}D{i:2}D{i:3}
}
##^##*/
