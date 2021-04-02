import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
    id: lockWindow
    width: 1000
    height: 580
    minimumWidth: 800
    minimumHeight: 500
    visible: true
    color: "#00000000"
    title: qsTr("CAIO")

    // Remove Title Bar
//  flags: Qt.Window | Qt.FramelessWindowHint

    Rectangle {
        id: bg
        color: "#16181d"
        radius: 0
        border.color: "#383e4c"
        border.width: 1
        anchors.fill: parent
        z: 1

        Rectangle {
            id: container
            color: "#00000000"
            anchors.fill: parent

            Label {
                id: labelLock
                color: "#ffffff"
                text: qsTr("LOCKED")
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 51
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                wrapMode: Text.WordWrap
                font.family: "Times New Roman"
                anchors.horizontalCenter: parent.horizontalCenter
            }
        }
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.66}
}
##^##*/
